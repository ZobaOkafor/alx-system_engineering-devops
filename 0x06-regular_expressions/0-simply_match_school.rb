#!/usr/bin/env ruby

puts ARGV.join(' ').scan(/\bSchool\b/).join('$').concat('$')
