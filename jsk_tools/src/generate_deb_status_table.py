#!/usr/bin/env python

import argparse
import collections
import sys

try:
    import tabulate
except ImportError:
    sys.stderr.write('Please install tabulate: pip install tabulate\n')
    sys.exit(1)

from rosdistro import get_index_url, get_index, get_distribution_files

def generate_deb_status_table(package):
    sys.stderr.write(';; Wringing DEB status table for {} ...\n'.format(package))
    print('[//]: # (!!DO NOT EDIT !!)\n')
    print('[//]: # (THIS SECTION IS AUTOMATICALLY GENERATED BY)\n')
    print('[//]: # (rosrun jsk_tools generate_deb_status_table.py {})\n'.format(package))
    print('')
    DISTROS = collections.OrderedDict()
    rosdistro_index = get_index(get_index_url())
    for distro, distro_info in sorted(rosdistro_index.distributions.items()):
        if not (distro_info['distribution_status'] != 'end-of-life' and \
                distro_info['distribution_type'] == 'ros1'):
            sys.stderr.write(';; Skipping {} because of {} and {} ...\n'.format(distro, distro_info['distribution_status'], distro_info['distribution_type']))
            continue
        distribution_files = get_distribution_files(rosdistro_index, distro)
        if len(distribution_files) > 1:
            sys.stderr.write('distribution_files has multiple entories {}\n'.format(distribution_files))
            sys.exit(1)
        platform = {}
        for platform_os in ['ubuntu', 'debian']:
            if platform_os in distribution_files[0].release_platforms:
                platform[platform_os] = distribution_files[0].release_platforms[platform_os]
        DISTROS[distro] = platform
        #print('DISTROS[{}] = {}'.format(distro, platform))

    table = []
    for bit, arch in zip(['v8', 'hf', '32', '64'],
                         ['arm64', 'armhf', 'i386', 'amd64']):
        if not table:  # first row
            headers = ['Package']
        row = ['{} ({})'.format(package, arch)]
        for distro, platform_list in DISTROS.items():
            for platform_os in ['ubuntu', 'debian']:
                if platform_os not in platform_list:
                    continue
                os_list = platform_list[platform_os]
                if ((distro >= 'melodic' and arch == 'i386')
                        or (platform_os == 'debian' and arch == 'armhf')):
                    template_md = '---'
                else:
                    for os in os_list:
                        if arch.startswith('arm'):
                            if platform_os == 'ubuntu' and 'precise' < os and os < 'xenial':
                                os_arch = 'arm_u'
                            else:
                                os_arch = '{platform_prefix}{prefix_os}{bit}_{platform_prefix}'
                                os_arch = os_arch.format(
                                    platform_prefix=platform_os[0], prefix_os=os[0], bit=bit)
                        elif platform_os == 'ubuntu':
                            os_arch = 'u'
                        else:
                            os_arch = '{platform_prefix}{prefix_os}_{platform_prefix}'
                            os_arch = os_arch.format(
                                platform_prefix=platform_os[0], prefix_os=os[0])

                        if not table:  # first row
                            headers.append(
                                '{} ({})'.format(distro.capitalize(), os.capitalize()))

                        url = 'http://build.ros.org/job/{prefix_ros}bin_{os_arch}{prefix_os}{bit}__{package}__{platform_os}_{os}_{arch}__binary'  # NOQA
                    url = url.format(
                        bit=bit,
                        arch=arch,
                        os_arch=os_arch,
                        prefix_os=os[0].upper(),
                        prefix_ros=distro[0].upper(),
                        package=package,
                        platform_os=platform_os,
                        os=os,
                    )
                    template_md = '[![Build Status]({url}/badge/icon)]({url})'
                row.append(template_md.format(url=url))
        table.append(row)

    print(tabulate.tabulate(table, headers=headers, tablefmt='pipe'))
    print('')
    print('[//]: #')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('package')
    args = parser.parse_args()

    package = args.package

    generate_deb_status_table(package)


if __name__ == '__main__':
    main()
