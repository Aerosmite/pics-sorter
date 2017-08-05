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
* The [LatLon package](https://pypi.python.org/pypi/LatLon)
```
$ pip install LatLon
```

### Installing

Once you download [file_sorter.py](file_sorter.py), open it with your favorite text-editing sofware.

Now go get your own API key [here](https://developers.google.com/maps/documentation/geocoding/start#get-a-key) and past it in `gmaps_key`.

Change the `dir_path` to the directory which contains all your pics **without any subdirectory**.

*optional: redefine the maximum distance or duration before spliting an event with* `distance_max` *and* `duration_max`. 

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
