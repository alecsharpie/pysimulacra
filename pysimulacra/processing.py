# from here https://github.com/JD-P/simulacra-aesthetic-captions/issues/1#issuecomment-1191765691

import pathlib
import tarfile


def reprocess_archives(path_input_base, path_output_base):
    archive_paths = list(sorted([p for p in path_input_base.glob('*.tar')]))

    for input_tar_path in archive_paths:
        path_output_dir = path_output_base / input_tar_path.stem

        if not path_output_dir.exists():
            path_output_dir.mkdir()

        with tarfile.open(name=input_tar_path, mode='r', bufsize=10240) as tf:
            print(f'Extracting {input_tar_path}...')

            file_ct = 0

            entry = tf.next()  # type: tarfile.TarInfo
            while entry is not None:
                if not entry.isfile(): continue

                # Replace prefix and leave only leading 'gid' and 'index' | sac-000000/123_1.png
                new_name = entry.name.replace(
                    'home/jdp/simulacra-aesthetic-captions/', '')
                name_parts = new_name.split('_')
                new_name = f'{name_parts[0]}_{name_parts[-1]}'

                path_output_file = path_output_dir / new_name

                # Override output filepath/name
                tf._extract_member(entry,
                                   str(path_output_file),
                                   set_attrs=False,
                                   numeric_owner=False)

                file_ct += 1
                entry = tf.next()
            print(f'  Extracted {file_ct} files.')


if __name__ == '__main__':
    path_input_base = pathlib.Path(
        r'raw_data/'
    )
    path_output_base = pathlib.Path(
        r'raw_data/new/')

    reprocess_archives(path_input_base, path_output_base)
