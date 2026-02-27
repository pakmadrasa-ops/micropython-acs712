# ADC Testing Utility

This script includes all test functions for ADC. The utility is used to test ADC functionality for values.

def test_adc_value_range():
    """Test if the ADC value is within the expected range."""
    adc_value = read_adc()
    assert 0 <= adc_value <= 1023, f"ADC value {adc_value} is out of range!"


def test_adc_accuracy():
    """Test if the ADC value matches the expected voltage levels."""
    expected_values = [0, 512, 1023]
    for expected in expected_values:
        adc_value = read_adc()
        assert adc_value == expected, f"Expected {expected}, but got {adc_value}"


def test_adc_noise():
    """Test if the ADC readings have minimal noise."""
    readings = [read_adc() for _ in range(100)]
    assert max(readings) - min(readings) < 10, "ADC readings are too noisy!"


def read_adc():
    """Mock function to read ADC value. Replace with actual read function."""
    return 512  # Dummy value for testing

if __name__ == '__main__':
    # Run tests
    test_adc_value_range()
    test_adc_accuracy()
    test_adc_noise()
    print("All tests passed!")