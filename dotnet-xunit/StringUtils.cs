namespace DotnetXunit;

public static class StringUtils
{
    public static string CamelCase(string str)
    {
        var parts = str.Split('-', '_');
        if (parts.Length == 0) return str;
        var result = parts[0].ToLower();
        for (int i = 1; i < parts.Length; i++)
        {
            if (parts[i].Length > 0)
                result += char.ToUpper(parts[i][0]) + parts[i].Substring(1).ToLower();
        }
        return result;
    }

    public static string Repeat(string str, int count)
    {
        var result = "";
        for (int i = 0; i < count; i++)
        {
            result += str;
        }
        return result;
    }

    public static bool IsPalindrome(string str)
    {
        var cleaned = new string(str.Where(char.IsLetterOrDigit).ToArray()).ToLower();
        var reversed = new string(cleaned.Reverse().ToArray());
        return cleaned == reversed;
    }

    public static int CountOccurrences(string str, char target)
    {
        return str.Count(c => c == target);
    }
}
