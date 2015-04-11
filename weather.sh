#!/bin/sh

URL='http://www.accuweather.com/en/nl/oudenbosch/249235/weather-forecast/249235'

wget -q -O- "$URL" | awk -F\' '/acm_RecentLocationsCarousel\.push/{print $1$10 }' | head -n 1 | cut -d ":" -f 3

