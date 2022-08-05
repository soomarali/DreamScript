#!/usr/bin/python
# -*- coding: utf-8 -*-
# code: BY MOHAMED_OS

from __future__ import print_function

from socket import socket, gethostname, AF_INET, SOCK_DGRAM
from os import system, popen, uname, path
from sys import version, version_info
from ssl import OPENSSL_VERSION as ssl
from datetime import datetime
from time import sleep
from json import loads
from re import match

try:
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
except ImportError:
    from urllib2 import Request, urlopen, URLError, HTTPError


# colors
C = "\033[0m"     # clear (end)
R = "\033[0;31m"  # red (error)
G = "\033[0;32m"  # green (process)
B = "\033[0;36m"  # blue (choice)
Y = "\033[0;33m"  # yellow (info)

URL = 'https://raw.githubusercontent.com/MOHAMED19OS/e2script/main/'

if hasattr(__builtins__, 'raw_input'):
    input = raw_input

PY = version_info.major


def info(item):
    try:
        req = Request('{}packages.json'.format(URL))
        req.add_header(
            'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0')
        response = urlopen(req)
        link = loads(response.read()).get(item)
        if item == 'package':
            if PY == 3:
                return list(map(lambda x: x.replace('python', 'python3'), link))
        return link
    except HTTPError as e:
        print('HTTP Error code: ', e.code)
    except URLError as e:
        print('URL Error: ', e.reason)


def banner():
    system('clear')
    print(B)
    print(r"""⠀⠀⡶⠛⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠚⢶⡀⠀
⢰⠛⠃⠀⢠⣏⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣤⣤⣄⣀⡀⠀⠀⠀⣸⠇⠀⠈⠙⣧
⠸⣦⣤⣄⠀⠙⢷⣤⣶⠟⠛⢉⣁⣤⣤⣤⣤⣀⣉⠙⠻⢷⣤⡾⠋⢀⣤⣤⣴⠏
⠀⠀⠀⠈⠳⣤⡾⠋⣀⣴⣿⣿⠿⠿⠟⠛⠿⠿⣿⣿⣶⣄⠙⢿⣦⠟⠁⠀⠀⠀
⠀⠀⠀⢀⣾⠟⢀⣾⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣷⡄⠹⣷⡀⠀⠀⠀
⠀⠀⠀⣾⡏⢠⣿⣿⡯⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠤⠤⠽⣿⣿⡆⠹⣷⡀⠀⠀
⠀⠀⢸⣟⣠⡿⠿⠟⠒⣒⣒⣉⣉⣉⣉⣉⣉⣉⣉⣉⣒⣒⡛⠻⠿⢤⣹⣇⠀⠀
⠀⠀⣾⡭⢤⣤⣠⡞⠉⠁⢀⣀⣀⠀⠀⠀⠀⢀⣀⣀⠀⠈⢹⣦⣤⡤⠴⣿⠀⠀
⠀⠀⣿⡇⢸⣿⣿⣇⠀⣼⣿⣿⣿⣷⠀⠀⣼⣿⣿⣿⣷⠀⢸⣿⣿⡇⠀⣿⠀⠀
⠀⠀⢻⡇⠸⣿⣿⣿⡄⢿⣿⣿⣿⡿⠀⠀⢿⣿⣿⣿⡿⢀⣿⣿⣿⡇⢸⣿⠀⠀
⠀⠀⠸⣿⡀⢿⣿⣿⣿⣆⠉⠛⠋⠀⢴⣶⠀⠉⠛⠉⣠⣿⣿⣿⡿⠀⣾⠇⠀⠀
⠀⠀⠀⢻⣷⡈⢻⣿⣿⣿⣿⣶⣤⣀⣈⣁⣀⡤⣴⣿⣿⣿⣿⡿⠁⣼⠏⠀⠀⠀
⠀⠀⠀⢀⣽⣷⣄⠙⢿⣿⣿⡟⢲⠧⡦⠼⠤⢷⢺⣿⣿⡿⠋⣠⣾⢿⣄⠀⠀⠀
⣰⠟⠛⠛⠁⣨⡿⢷⣤⣈⠙⢿⡙⠒⠓⠒⠒⠚⡹⠛⢁⣤⣾⠿⣧⡀⠙⠋⠙⣆
⠹⣤⡀⠀⠐⡏⠀⠀⠉⠛⠿⣶⣿⣶⣤⣤⣤⣾⣷⠾⠟⠋⠀⠀⢸⡇⠀⢠⣤⠟
⠀⠀⠳⢤⠾⠃⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠘⠷⠤⠾⠁⠀""")
    print(C)
    print("   Written by {}MOHAMED_OS{} (͡๏̯͡๏) {}ver{}: {}\n".format(
        B, C, R, C, info('version')))
    print((datetime.now().strftime("%d-%m-%Y %X")).rjust(25))


def image():
    global status, update, install
    if path.exists('/etc/opkg/opkg.conf'):
        status = '/var/lib/opkg/status'
        update = 'opkg update >/dev/null 2>&1'
        install = 'opkg install'
    else:
        status = '/var/lib/dpkg/status'
        update = 'apt-get update >/dev/null 2>&1'
        install = 'apt-get install'
    return path.exists('/etc/opkg/opkg.conf')


def check():
    package_list = info('package')
    with open(status) as f:
        for c in f.readlines():
            if c.startswith('Package:'):
                pkg = c[c.index(' '):].strip()
                while (package_list.count(pkg)):
                    package_list.remove(pkg)
    return package_list


def shell(cmd): return popen(cmd).read().strip()


def get_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def DataBuild():
    try:
        if path.isfile('/usr/lib/enigma.info'):
            build = open('/usr/lib/enigma.info').readlines()
            for c in build:
                if match('compiledate', c):
                    data = c.split('=')[-1].strip()
        elif path.isfile('/etc/version'):
            build = open('/etc/version').read().strip()
            data = build[:8]

        if data.isdigit():
            return datetime.strptime(data, '%Y%m%d').strftime('%Y-%m-%d')
        else:
            return data
    except:
        return 'unknown'


def DistroImage():
    try:
        if path.isfile('/etc/issue'):
            image_type = open("/etc/issue").readlines()[-2].strip()[:-6]
            return image_type.capitalize().replace("develop", "Nightly Build")
        elif path.isfile('/usr/lib/enigma.info'):
            distro = open('/usr/lib/enigma.info').readlines()
            for c in distro:
                if match('distro', c):
                    return c.split('=')[-1].strip().capitalize()
    except:
        return 'undefined'


def system_info():

    ram = shell("free | grep Mem  | awk '{ print $4 }'")
    disk = shell("df -h | awk 'NR == 2 {print $4}'")

    system('clear')
    print(Y)
    print(r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣾⣿⣿⣿⣿⣿⣿⣷⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⣀⣠⣿⣿⣄⣀⡀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⡟⠀⠀⣀⣴⣾⣿⠿⠿⠿⠿⠿⠿⢿⣷⣦⣄⠀⠀⠻⣿⣄⠀⠀⠀
⠀⠀⣴⣿⠋⠀⣠⣾⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣦⡀⠘⣿⣧⠀⠀
⠀⣼⣿⣿⣷⣾⡿⢋⣤⣶⣶⣦⣄⠀⠀⠀⠀⢀⣤⣶⣶⣤⡘⢿⣿⣿⣿⣿⣧⠀
⢰⣿⠃⠀⣿⡿⢁⣾⣿⣿⣿⣿⣿⣇⠀⠀⢠⣿⣿⣿⣿⣿⣿⡆⢻⣿⡇⠈⣿⣇
⢿⡏⠀⢸⣿⠇⠘⣿⣿⣿⣿⣿⣿⡟⠀⠀⢸⣿⣿⣿⣿⣿⣿⠇⠈⣿⣧⠀⠸⣿
⠀⠀⠀⣾⣿⠀⠀⠘⠿⣿⣿⡿⠏⠀⢀⡀⠀⠙⢿⣿⣿⡿⠋⠀⠀⢹⣿⠀⠀⠀
⠀⠀⠀⢿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠺⠟⠀⠀⠀⠀⠀⠀⣀⣀⣀⣸⣿⠀⠀⠀
⢿⣧⠀⢸⣿⡟⠛⣿⡿⠿⠿⣿⠿⠿⢿⣿⠿⠿⣿⡿⠿⢿⣿⠟⠻⣿⡿⠀⣸⣿
⠸⣿⣆⢀⣿⣷⡀⢸⡇⠀⠀⣿⠀⠀⢸⣿⠀⠀⣿⡇⠀⢸⣿⠀⣼⣿⡇⢠⣿⠇
⠀⠹⣿⣿⡿⢿⣷⣿⡇⠀⠀⣿⠀⠀⢸⣿⠀⠀⣿⡇⠀⢸⣿⣾⣿⠿⣿⣿⡟⠀
⠀⠀⠹⣿⣦⠀⠙⢿⣿⣤⣠⣿⡆⠀⢸⣿⠀⠀⣿⣷⣠⣾⡿⠟⠁⣰⣿⠟⠀⠀
⠀⠀⠀⠈⢿⣷⡀⠀⠉⠻⢿⣿⣷⣶⣾⣿⣶⣶⣿⡿⠟⠋⠀⠀⣼⡿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠀⠀⠀⢀⣀⠀⠉⠙⣿⣿⠋⠉⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⠿⣿⣿⣿⣿⣿⣿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    print(C, end='')
    print("Machine: {}".rjust(18).format(gethostname()))
    print("Architecture: {}".rjust(18).format(uname()[4]))
    print("ImageDistro: {}".rjust(18).format(DistroImage()))
    print("ImageBuild: {}".rjust(18).format(DataBuild()))
    print("OpenSSL: {}".rjust(18).format(ssl.split()[1]))
    print("Python: {}".rjust(18).format(version.split()[0]))
    print("Gcc: {}".rjust(18).format(version.split()[-1].strip(']')))
    print("FreeRAM: {} KB".rjust(21).format(ram))
    print("FreeDisk: {} GB".rjust(21).format(disk))
    print("IPaddress: {}".rjust(18).format(get_ip()))


def prompt(choices):

    options = list(choices)
    while True:
        print(
            "{}(?){} Choose an option [{}-{}] : ".format(B, C, options[0], options[-1]), end='')
        choice = [str(x).upper() for x in input().split()]

        for name in choice:
            if name not in options:
                print("\n{}(!){} Select one of the available options !!\n".format(R, C))
                continue
        return list(dict.fromkeys(choice))


def main():
    image()

    passwd = shell("passwd -S | awk '{print$2}'")

    system_info()
    sleep(5)

    if passwd == 'NP':
        print('{}(!){} Please Enter {}Password{} For {}{}{} : '.format(
            R, C, Y, C, B, DistroImage(), C), end='')
        root = input()
        system("echo 'root:{}' | chpasswd".format(root))

    if check():
        system(update)
        for name in check():
            system('clear')
            print("   >>>>   {}Please Wait{} while we Install {}{}{} ...".format(
                G, C, Y, name, C))
            system('{} {}'.format(install, name))

    emu = info('plugins')
    cam = {
        "A": emu['novalertv'],
        "B": emu['quran'],
        "C": emu['ajpanel'],
        "D": emu['arabic_savior'],
        "E": emu['youtube'],
        "F": emu['iptosat'],
        "G": emu['e2iplayer'],
        "H": emu['suptv'],
        "I": emu['multi_stalker'],
        "J": emu['ipaudio'],
        "K": emu['keyadder'],
        "L": emu['fonotonsat'],
        "M": emu['newvirtualkeyBoard'],
        "N": emu['epg_grabber'],
        "O": emu['emu'],
        "P": emu['neoboot'],
        "Q": emu['flashonline'],
        "R": emu['xtraevante'],
        "S": emu['dreamsatpanel'],
        "T": emu['jedimakerxtream'],
        "U": emu['xstreamity'],
        "V": emu['xc_code'],
        "W": emu['openmultiboot'],
        "X": emu['subssupport'],
        "Y": emu['backupflash'],
        "Z": emu['raedquicksignal']
    }

    system('clear')
    print(
        "\n{}(?){} \033[0;33mChoose the Plugin Install\033[0m :".format(B, C))

    menu = """
    (A) NovalerTV       (H) Suptv               (O) EMU             (V) XcPlugin Forever
    (B) Quran           (I) Multi_Stalker       (P) NeoBoot         (W) OpenMultiboot
    (C) AjPanel         (J) IPAudio             (Q) FlashOnline     (X) SubsSupport
    (D) ArabicSavior    (K) KeyAdder            (R) XtraEvent       (Y) BackupFlash
    (E) YouTube         (L) FootOnsat           (S) DreamSatPanel   (Z) RaedQuickSignal
    (F) IPtoSAT         (M) NewVirtualKeyBoard  (T) JediMakerXtream
    (G) E2IPLAYER       (N) EPG Grabber         (U) Xstreamity
    """

    print(menu)

    for name in prompt(cam.keys()):
        system(cam.get(name))
        sleep(5)

    if image():
        system('killall -9 enigma2')
    else:
        system('systemctl restart enigma2')


if __name__ == '__main__':
    main()
    banner()
