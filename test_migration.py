# test_mtcnn_integration.py
try:
    import tensorflow as tf
    from tensorflow.keras import layers
    from mtcnn import MTCNN

    print("Imports successful!")
    detector = MTCNN()
    print("MTCNN initialization successful!")
except Exception as e:
    print(f"Error during import or initialization: {e}")
