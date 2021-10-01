import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from codecarbon import EmissionsTracker #Energy Usage


#@track_emissions(project_name="asd screening")

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.1):
            print("\n accuracy")
            self.model.stop_training = True

tracker = EmissionsTracker()

def main():
    mnist = tf.keras.datasets.fashion_mnist
    # Load MNIST dataset
    (input_train, training_labels), (input_test, test_labels) = mnist.load_data()

    # Set input shape -->
    # https://www.machinecurve.com/index.php/question/valueerror-input-0-of-layer-sequential-is-incompatible-with-the-layer-expected-min_ndim4-found-ndim3-full-shape-received-250-28-28/
    sample_shape = input_train[0].shape
    img_width, img_height = sample_shape[0], sample_shape[1]
    input_shape = (img_width, img_height, 1)

    # Reshape data 
    training_images = input_train.reshape(len(input_train), input_shape[0], input_shape[1], input_shape[2])
    test_images  = input_test.reshape(len(input_test), input_shape[0], input_shape[1], input_shape[2])
    #-->

    #Image in index 0
    #plt.imshow(training_images[0])
    #print(training_labels[0])
    #print(training_images[0])

    #Image in index 42
    #plt.imshow(training_images[42])
    #print(training_labels[42])
    #print(training_images[42])

    training_images = training_images/255.0
    test_images = test_images/255.0 
    callbacks = myCallback()

    model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(64, (3,3), activation = 'relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

    model.compile(optimizer = 'adam', loss='sparse_categorical_crossentropy')
    model.summary()
    model.fit(training_images, training_labels, epochs = 5)
    test_loss = model.evaluate(test_images, test_labels)
    print("Test Loss: ",test_loss)

if __name__ == "__main__":
    tracker.start()
    main()
    emi: float=tracker.stop()
    print(f"overall emmisions:{emi} kg")
    emi= emi*89875517873681764
    print(f"overall emmisions:{emi} joules")
