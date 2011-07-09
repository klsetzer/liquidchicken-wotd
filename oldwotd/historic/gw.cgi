#!/usr/bin/perl
use strict;
use warnings;

use Net::Google::Calendar;

my $url='https://www.google.com/calendar/feeds/u6g675oejpdha4pncv50rmi8tc%40group.calendar.google.com/private-b56901af5fe64ee8aab475632d2ab8f0/basic';

my $cal = Net::Google::Calendar->new( url => $url);

for ($cal->get_events()) {
	print $_->title."\n";
	print $_->content->body."\n*****\n\n";
}



