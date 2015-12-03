#!/usr/bin/ruby
# -*- coding: utf-8 -*-

require "cgi"
require 'rubygems'
require 'sqlite3'

cgi = CGI.new()
word = Array.new
words = Array.new
d = Array.new
data = CGI.new()
#dct = Array.new
i = 0

print "Content-type: text/html; charset=utf-8\n\n"

 userdb = SQLite3::Database.new("users")
 userdb.execute("SELECT * FROM users")

 text = data["word"]
# text = "Do you like apple? I like apples."
# puts "入力したテキスト"
# puts text
 text.chomp!
# sentence = text.split(".")
# sentence = text.split("?")
# puts "文１"
# puts sentence[0]
 words = text.gsub(/[\.,?!()*:;{}~=|'&%0123456789]/,'').downcase
 word = words.split(" ")
 word.uniq!
# puts "単語"
# puts word[0]

# print "それに含まれる単語</br>"
# i = 0
# for i in 0..word.length-1
#     word = word[i].gsub(/[\.,?!()*:;{}~=|'&%0123456789]/,'')
#     print '<a href="http://ejje.weblio.jp/content/'+wd+'">'
#     print wd
#     print '<a>'
#     print" </br>"
      #update(dict, newword, wd.downcase)
#     i = i + 1
# end

 k = 0
# print word
# print sentence[0]
#  while k < sentence.length do
#     userdb.execute("INSERT INTO review values (1,'#{sentence[k]}', '#{word}')")
#     k = k + 1
# end
userdb.close() 

 dictdb = SQLite3::Database.new("dictionary.sqlite3")
 dictdb.execute("SELECT * FROM items")
 i = 0
 while i < word.length do
     dict = dictdb.execute("SELECT * FROM items WHERE word == '#{word[i]}'")
     d.push(dict[0][2])
    i = i + 1
 end
 dictdb.close()

 j = 0
 fo = open("json.txt", "w")
 fo.write('{')

 while j < word.length do
    fo.write('"')
    fo.write("#{word[j]}")
    fo.write('": "')
    fo.write("#{d[j]}")
    if j == word.length-1
        fo.write('"}')
    else
        fo.write('",')
    end
    j = j + 1
 end
 fo.close()

  fh = open("json.txt", "r")
  while line = fh.gets
    print line.chomp + "\r\n"
  end
  fh.close


