import typesystem


class Example(typesystem.Schema):
    a = typesystem.String(max_length=10)
    b = typesystem.Integer(maximum=5)


def test_validation_result_repr():
    result = Example.validate({"a": "a", "b": 1})
    assert repr(result) == "ValidationResult(value=Example(a='a', b=1))"

    result = Example.validate({"a": "a"})
    assert (
        repr(result)
        == "ValidationResult(error=ValidationError([Message(text='This field is required.', code='required', index=['b'])]))"
    )


def test_validation_error_repr():
    result = Example.validate({"a": "a"})
    assert (
        repr(result.error)
        == "ValidationError([Message(text='This field is required.', code='required', index=['b'])])"
    )

    result = typesystem.String(max_length=10).validate("a" * 100)
    assert (
        repr(result.error)
        == "ValidationError(text='Must have no more than 10 characters.', code='max_length')"
    )


def test_validation_message_repr():
    result = Example.validate({"a": "a"})
    message = result.error.messages()[0]
    assert (
        repr(message)
        == "Message(text='This field is required.', code='required', index=['b'])"
    )

    result = typesystem.String(max_length=10).validate("a" * 100)
    message = result.error.messages()[0]
    assert (
        repr(message)
        == "Message(text='Must have no more than 10 characters.', code='max_length')"
    )