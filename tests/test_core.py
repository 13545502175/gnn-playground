from gnn_playground import train_demo

def test_training_respects_requested_shape():
    result = train_demo(layers=3, epochs=4)
    assert result['config']['layers'] == 3
    assert len(result['history']) == 4
    assert len(result['predictions']) == 5
