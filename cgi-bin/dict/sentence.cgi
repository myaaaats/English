#!/usr/bin/ruby
# -*- coding: utf-8 -*-

require "cgi"
require 'rubygems'

cgi = CGI.new()
#word = Array.new
words = Array.new
wd = Array.new
#sentence = Array.new
d = Array.new
data = CGI.new()
#dict = Array.new
i = 0
text = "I am a girl, Maya. Who are you?"

print "Content-type: text/html; charset=utf-8\n\n"

 text.chomp!
 sentence = text.split(/[.?*:'"();|]/)
 puts "＊文章１＊"
 puts sentence[0]
 puts "＊文章２＊"
 puts sentence[1]
 puts "\n"
# puts "文末記号を付ける処理(これはDBに送る直前でいい)"
# puts sentence[0].concat(".")
# puts sentence[1].concat("?")
# puts "\n"
 sentence[0].strip!
 sentence[1].strip!
 puts "文章１のスペースの数"
 puts sentence[0].count(" ")
 puts "文章２のスペースの数"
 puts sentence[1].count(" ")
 puts "---------------------------------"
 words = text.gsub(/[\.,?!()*:;{}~=|'&%0123456789]/,'').downcase
 puts "＊いらないものを全て空白にする＊"
 puts words
 puts "\n"
 puts "＊空白でsplit＊"
 word = words.split(" ")
 puts word

 i = 0
 while i < 5 do
     wd.push("#{word[i]}")
     i = i + 1
 end
# while i <= 7 do
#     wd[1].push("#{word[i]}")
#     i = i + 1
# end
 puts "＊文１の単語"
 puts wd
# puts "＊文２の単語"
# puts wd[1]
 
 # word.uniq!
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

