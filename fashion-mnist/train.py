import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from codecarbon import EmissionsTracker #Energy Usage


tracker = EmissionsTracker()
#@track_emissions(project_name="asd screening")

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.1):
            print("\n accuracy")
            self.model.stop_training = True

def main():
    mnist = tf.keras.datasets.fashion_mnist
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data()

    #Image in index 0
    plt.imshow(training_images[0])
    #print(training_labels[0])
    #print(training_images[0])

    #Image in index 42
    plt.imshow(training_images[42])
    #print(training_labels[42])
    #print(training_images[42])

    training_images = training_images/255.0
    test_images = test_images/255.0

    

    callbacks = myCallback()

    model = tf.keras.Sequential([keras.layers.Flatten(), 
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy')
    model.fit(training_images, training_labels, epochs = 130, callbacks = [callbacks])
    test_accuracy = model.evaluate(test_images, test_labels)
    train_accuracy = model.evaluate(training_images, training_labels)
    print("Test Accuracy: ",test_accuracy)
    print("Train Accuracy: ",train_accuracy)


if __name__ == "__main__":
    tracker.start()
    main()
    emi: float=tracker.stop()
    print(f"overall emmisions:{emi} kg")
    emi= emi*89875517873681764
    print(f"overall emmisions:{emi} joules")
