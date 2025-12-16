# GekiChu Song Sorter
A fun way to manually merge sort a looot of music to make a song ranking.

## Developer notes

All of the song data is found at [src/fnc_data_song.js](./src/fnc_data_song.js), defined in the array `ary_SongData`. Each song's data is an array with a specific number of elements; for example:

```js
["girls.exe", new Set([TITLE.ONGEKI_REFRESH]), { title: "ONGEKI_REFRESH" }, "t0xj5ZxWU3c", "rintaro soma", ORIGINAL_TRACK, GAME_VERSION]
```

The elements, in order, are as follows:

0. Track name.
1. A set containing IDs of the titles that the track appears in
2. An object specifying which title data to use when displaying this track.
3. YouTube video ID.
4. The track's artist
5. Always `ORIGINAL_TRACK`.
6. `GAME_VERSION` if the entry is the game size version, or `EXTENDED_VERSION` if the entry is an extended/long version.

### Adding new games/albums

* Add its title and related data to `TITLE`.
* Add its image to the [images](./images/) folder (180x180 preferably).
* Add its tracks to the end of `ary_SongData` in the above format
