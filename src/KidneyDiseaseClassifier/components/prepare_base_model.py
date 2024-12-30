import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from KidneyDiseaseClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        # Load the VGG16 base model
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            include_top=self.config.params_include_top,
            weights=self.config.params_weights
        )

        # Save the base model
        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        # Freeze layers as specified
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        # Add custom layers to the base model
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation='softmax'
        )(flatten_in)

        # Create a new model with the updated architecture
        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )

        # Recreate the optimizer for the new model
        optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

        # Compile the full model with the new optimizer
        full_model.compile(
            optimizer=optimizer,
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )

        # Print the model summary
        full_model.summary()
        return full_model

    def update_base_model(self):
        # Prepare the full model
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        # Save the updated model
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path, model):
        # Save the model to the specified path
        model.save(path)