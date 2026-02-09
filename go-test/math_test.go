package math

import "testing"

func TestAdd(t *testing.T) {
	if Add(2, 3) != 5 {
		t.Error("expected 2+3 = 5")
	}
	if Add(-1, 1) != 0 {
		t.Error("expected -1+1 = 0")
	}
}

func TestSubtract(t *testing.T) {
	if Subtract(10, 4) != 6 {
		t.Error("expected 10-4 = 6")
	}
}

func TestMultiply(t *testing.T) {
	if Multiply(3, 4) != 12 {
		t.Error("expected 3*4 = 12")
	}
}

func TestDivide(t *testing.T) {
	result, err := Divide(10, 2)
	if err != nil {
		t.Errorf("unexpected error: %v", err)
	}
	if result != 5 {
		t.Errorf("expected 10/2 = 5, got %f", result)
	}
}

func TestDivideByZero(t *testing.T) {
	_, err := Divide(1, 0)
	if err == nil {
		t.Error("expected error for division by zero")
	}
}
