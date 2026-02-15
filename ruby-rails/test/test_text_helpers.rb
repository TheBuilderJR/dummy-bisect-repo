require "test_helper"

class TestTextHelpers < Minitest::Test
  def test_titleize
    assert_equal "Hello World", TextHelpers.titleize("hello world")
    assert_equal "The Quick Brown Fox", TextHelpers.titleize("the quick brown fox")
    assert_equal "Ruby On Rails", TextHelpers.titleize("ruby on rails")
  end

  def test_truncate_words
    assert_equal "the quick...", TextHelpers.truncate_words("the quick brown fox", 2)
    assert_equal "hello world", TextHelpers.truncate_words("hello world", 5)
    assert_equal "one...", TextHelpers.truncate_words("one two three", 1)
  end

  def test_parameterize
    assert_equal "hello-world", TextHelpers.parameterize("Hello World")
    assert_equal "foo-bar", TextHelpers.parameterize("  Foo  Bar  ")
    assert_equal "test-123", TextHelpers.parameterize("Test! @123#")
  end

  def test_humanize
    assert_equal "Hello world", TextHelpers.humanize("hello_world")
    assert_equal "Foo bar baz", TextHelpers.humanize("foo-bar-baz")
    assert_equal "My variable", TextHelpers.humanize("my_variable")
  end
end
