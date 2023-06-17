import os
import re

import rich_click as click

click.rich_click.USE_RICH_MARKUP = True


@click.command()
@click.argument("directory", type=click.Path(exists=True, dir_okay=True), default=".")
@click.argument("pattern", type=click.STRING)
@click.argument("prefix", default="")
@click.option(
    "--padding",
    "-p",
    type=int,
    default=1,
    show_default=True,
    help="Increases zero padding, with a padding of 3 files will be 001.",
)
@click.option(
    "--dry-run", "-d", is_flag=True, help="Perform a dry run without renaming files."
)
def bulk_rename(directory, pattern, prefix, padding, dry_run):
    """
    Bulk rename files in a directory with a given pattern, prefix and padding.

    Default directory is the current one.

    Files will be renamed incrementally. e.g: file1, file2, ...

    Pattern must be a regex.

    Prefix is optional.

    [yellow bold]Example Usage:[/]

    [i]Rename all files with png and jpg extension[/]

    [b]bulk_rename path/to/dir/ ".*.(png|jpg)"[/]

    [i]Rename all files that contain "image", add prefix "Wallpaper" with 2 padding[/]

    [b]bulk_rename path/to/dir/ "image*" "Wallpaper" -p 2[/]

    """
    file_list = os.listdir(os.path.expanduser(directory))
    file_list.sort()

    for i, file_name in enumerate(file_list):
        item_path = os.path.join(directory, file_name)
        if re.match(pattern, file_name) and os.path.isfile(item_path):
            file_name_parts = os.path.splitext(file_name)
            new_file_name = f"{prefix}{str(i+1).zfill(padding)}{file_name_parts[1]}"

            old_file = os.path.join(directory, file_name)
            new_file = os.path.join(directory, new_file_name)

            if not dry_run:
                os.rename(old_file, new_file)

            click.echo(f"Renamed: {file_name} -> {new_file_name}")


if __name__ == "__main__":
    bulk_rename()
