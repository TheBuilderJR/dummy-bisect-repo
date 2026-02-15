# Text processing helpers for the Rails application.

module TextHelpers
  def self.titleize(str)
    str.strip.split.map(&:capitalize).join(" ")
  end

  def self.truncate_words(str, count)
    words = str.split
    return str if words.length <= count
    words[0...count].join(" ") + "..."
  end

  def self.parameterize(str)
    str.downcase.strip.gsub(/[^a-z0-9\s-]/, "").gsub(/[\s]+/, "-")
  end

  def self.humanize(str)
    str.gsub(/[_-]/, " ").strip.capitalize
  end
end
