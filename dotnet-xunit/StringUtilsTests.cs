using Xunit;

namespace DotnetXunit;

public class StringUtilsTests
{
    [Fact]
    public void CamelCase_ConvertsDashedStrings()
    {
        Assert.Equal("helloWorld", StringUtils.CamelCase("hello-world"));
        Assert.Equal("fooBarBaz", StringUtils.CamelCase("foo-bar-baz"));
        Assert.Equal("hello", StringUtils.CamelCase("hello"));
    }

    [Fact]
    public void Repeat_RepeatsStringNTimes()
    {
        Assert.Equal("abcabcabc", StringUtils.Repeat("abc", 3));
        Assert.Equal("xx", StringUtils.Repeat("x", 2));
        Assert.Equal("", StringUtils.Repeat("hello", 0));
    }

    [Fact]
    public void IsPalindrome_DetectsPalindromes()
    {
        Assert.True(StringUtils.IsPalindrome("racecar"));
        Assert.True(StringUtils.IsPalindrome("A man a plan a canal Panama"));
        Assert.False(StringUtils.IsPalindrome("hello"));
    }

    [Fact]
    public void CountOccurrences_CountsCharacter()
    {
        Assert.Equal(3, StringUtils.CountOccurrences("hello world", 'l'));
        Assert.Equal(0, StringUtils.CountOccurrences("hello", 'z'));
        Assert.Equal(2, StringUtils.CountOccurrences("banana", 'n'));
    }
}
