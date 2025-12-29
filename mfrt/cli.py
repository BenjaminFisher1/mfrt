import click
import os

@click.command()
@click.option('--path', default='.', prompt='Path to directory (leave blank for current working directory)', help='Path to directory containing files to rename')
@click.option('--nameconvention', default='file', prompt='Naming convention', help='Naming convention for renamed files')
def main(path, nameconvention):
    """Lightweight Program to rename files in bulk based on a specified naming convention."""
    click.echo(f'Renaming files in {path} using naming convention: {nameconvention}')


    #Create list of FILES in directory, ignoring subdirectories
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    files.sort()  

    for i, file in enumerate(files, 1):
        old_name = os.path.join(path, file)

        #get extension
        _, extension = os.path.splitext(file)

        #Create new name with extension
        new_name = f"{nameconvention}_{i}{extension}"
        new_path = os.path.join(path, new_name)

        click.echo(f'Renaming "{file}" to "{new_name}"')
        os.rename(old_name, new_path)

    click.echo('Renaming complete.')
