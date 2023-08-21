from pathlib import Path


if __name__ == '__main__':
    new_folder = Path('new')
    new_folder.mkdir()

    for i, f in enumerate(Path('old').glob('*.json')):
        f.rename(new_folder / f'{i + 1}.json')