import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import matplotlib.pyplot as plt

# Simulate synthetic traffic data
def generate_data(samples=100):
    X = np.random.rand(samples, 4)  # inputs: vehicle counts in N, S, E, W
    y = (X[:, 0] + X[:, 1]) / (X[:, 2] + X[:, 3] + 1e-5)  # ratio N/S to E/W
    y = np.clip(y / np.max(y), 0, 1).reshape(-1, 1)
    return X, y

# Generate training data
X_train, y_train = generate_data()

# Build the model
model = models.Sequential([
    layers.Dense(16, activation='relu', input_shape=(4,)),
    layers.Dense(8, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # output: normalized green time ratio
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Enhancements: EarlyStopping
early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=5)

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop]
)

# Evaluate model
X_test, y_test = generate_data()
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f'Test Loss: {test_loss:.4f}, Test MAE: {test_mae:.4f}')