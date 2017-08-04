# pics-sorter

A simple use of exif data with python to group pics by places and periods.

## Getting Started

To make it works, you have to follow these following instructions.

### Prerequisites

* [Pip](https://pip.pypa.io/en/stable/installing/) (if it is not done yet)
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

Now go get your own API key [here](https://developers.google.com/maps/documentation/geocoding/start#get-a-key) and past the key in `gmaps_key`.

Change the `dir_path` to the directory which contains all your pics **without any subdirectory**.

*optional* Redefine the maximum distance or duration before spliting an event with `distance_max and duration_max`. 

### Launching

**Don't forget to make a backup first**.
*Mac*
```
python /Path/to/file_sorter.py
```

## Contributing

Any improvement will be greatly appreciated.
If you have a faster way to get exif data from pics / mov files, feel free to contribute !

# Authors

* **Mathieu Menoux** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

* A big thanks for the awesone [Exiftool](http://owl.phy.queensu.ca/~phil/exiftool/)
* Hat tip to anyone who's code was used
