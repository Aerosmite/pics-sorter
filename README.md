# pics-sorter

A simple use of exif data with python to group pics by places and periods. A good partner for people who have just too many files to sort !

## Getting Started

### Prerequisites

* [Pip](https://pip.pypa.io/en/stable/installing/)
* [Exiftool](http://owl.phy.queensu.ca/~phil/exiftool/) by Phil Harvey (needs to be in the root directory)
* The [googlemaps package](https://github.com/googlemaps/google-maps-services-python)
```
$ pip install -U googlemaps
```

### Installing

Once you download [file_sorter.py](file_sorter.py), open it with your favorite text-editing sofware.

Now go get your own API key [here](https://developers.google.com/maps/documentation/geocoding/start#get-a-key) and past it in `gmaps_key`.

Change the `dir_path` to the directory which contains all your pics **without any subdirectory**.

Other editable values:
* `distance_max`: the maximum distance before spliting an event
* `duration_max`: the maximum duration before spliting an event
* `Month`: edit it for you own language
* `is_nonGPS_allowed`: allow files with no GPS data (only creation date)
* `is_nonGPS_merge_allowed` : allow events with same date and no GPS data to merge 

### Launching

**Don't forget to make a backup first**.

Execute it like a basic .py program

### How it works ?

The program collect the `GPS` and `CreationDate` data of all files in dir_path using Exiftool.

Then, it test the distance and the duration between each: if it's higher than `distance_max` or `duration_max`, it groups all the previous matching files into one folder, named by the place and the period.

## Contributing

Any improvement will be greatly appreciated.
If you have a faster way to get exif data from pics / mov files, feel free to contribute !

### Authors

* **Mathieu Menoux** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* A big thanks for the awesone [Exiftool](http://owl.phy.queensu.ca/~phil/exiftool/)
* Hat tip to anyone who's code was used
