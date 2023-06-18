# Bulk Rename

Simple bulk rename tool, rename files in a directory with a given pattern, prefix and padding.

Rename is made using regex, also possible to sort and limit files to rename.

Written in python with [rich_click](https://github.com/ewels/rich-click/).

## Example Usage

**Rename all files with png and jpg extension**

`bulk_rename path/to/dir/ ".*.(png|jpg)"`

**Rename all files that contain "image", add prefix "Wallpaper" with 2 padding**

`bulk_rename path/to/dir/ "image*" "Wallpaper" -p 2`

**Rename all files limited to 10, sorted by size**

`bulk_rename path/to/dir/ "*" -l 10 -s size`

**More info using --help**

`bulk_rename --help`

## **Friendly Reminder**

This tool will rename any file that you have permissions, and can cause damage, specially on UNIX systems, so please be careful and use it with caution. I advise to run using `--dry-run` flag first.
