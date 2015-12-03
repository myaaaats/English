#!/usr/bin/ruby
# -*- encoding: utf-8 -*-

 require 'cgi'
 require 'rubygems'
 require 'sqlite3'

 print "Content-type: text/html; charset=utf-8\n\n"

 def update(dict, newwd, word)
     if dict[word]==nil
         dict[word] = 1
         newwd.push(word)
     else
         dict[word] = dict[word] + 1
     end
 end

 def normalize_pl(wordd)
     if wordd.slice(-1..-1) == "s"
         return wordd.slice(0..-2)
     else
         return wordd
     end
 end

 data = CGI.new

 udb = SQLite3::Database.new("users")
 udb.execute("SELECT * FROM users")

 userinfo = udb.execute("SELECT * FROM users WHERE user_id = 1")
 u= Array.new
 user = Array.new
 userword = Array.new
 usercount = Array.new
 user = {}
 userinfo.each do |tuple|
     tuple[0].force_encoding("utf-8")
     tuple[1].force_encoding("utf-8")
     tuple[2].force_encoding("utf-8")
     tuple[3].force_encoding("utf-8")
     u.push(tuple)
 end
 udb.close

 hh = open("data/user.txt","w")
 user.each_key{|name|
     hh.write("#{name}")
     hh.write(",")
     hh.write(user[name].to_s)
     hh.write("\n")
 }
 hh.close()

 h = open("data/user.txt","r")
 num = 0

 dict = Hash.new
 newword = Array.new

 while(line = h.gets)
     w = line.chomp
#     d = w.force_encoding("utf-8").split(",")
     d = w.split(",")
     dict[d[0]] = d[1].to_i
 end

 text = data["word"]
# print "入力したテキスト</br>"
# print text + "</br></br>"

 word = text.chomp
 words = word.split(" ")

# print "それに含まれる単語</br>"
## puts "入力された英文</br>"
 i = 0
 updatedb = SQLite3::Database.new("users")
 updatedb.execute('SELECT * FROM users')

 for i in 0..words.length-1
      wd = words[i].gsub(/[\.,?!()*:;{}~=|'&%0123456789]/,'')
      print '<a href="http://ejje.weblio.jp/content/'+wd+'">'
      print wd
      print '</a>'
      print " "
      update(dict, newword, wd.downcase)
  end
  h.close()
##   puts "."
#  print "</br></br>あなたは"
#  print  dict.length
#  print "語の英単語に出会ったことがあります。 </br>"

  dict.each_key{|name|
      updatedb.execute("UPDATE users SET count = #{dict[name]} WHERE word = '#{name}'")
  }


#  puts newword[0]
  updatedb.close()
#  puts "これはデバックです"
#  puts newword.length
#  puts "cat"
#  puts newword[0]

  insertdb = SQLite3::Database.new("users")
  insertdb.execute('SELECT * FROM users')
  j = 0
  while j < newword.length do
#      puts "#{newword}"
      insertdb.execute("INSERT INTO users values (1,'know','#{newword[j]}',1)")
      j = j + 1
  end

  insertdb.close()
#  print "</br>"
#  print "新出単語"
#  print newword
#  print "</br>"
#  print dict
#  print "</br>"
