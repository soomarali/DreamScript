# -*- coding: utf-8 -*-
# code: BY MOHAMED_OS


from __future__ import print_function

from json import loads
from os import chdir, popen, remove, system
from os.path import isfile, join
from re import MULTILINE, findall, match
from socket import gethostname
from sys import version_info
from tarfile import TarFile
from time import sleep

if version_info[0] == 3:
    from urllib.error import HTTPError, URLError
    from urllib.request import Request, urlopen, urlretrieve
else:
    from urllib import urlretrieve

    from urllib2 import HTTPError, Request, URLError, urlopen

# colors
C = "\033[0m"     # clear (end)
R = "\033[0;31m"  # red (error)
G = "\033[0;32m"  # green (process)
B = "\033[0;36m"  # blue (choice)
Y = "\033[0;33m"  # yellow (info)


if hasattr(__builtins__, 'raw_input'):
    input = raw_input


class Script():

    URL = 'https://raw.githubusercontent.com/MOHAMED19OS/e2script/main/'

    def __init__(self):
        self.list_pkg = []
        self.hostname = gethostname()
        self.package = ['wget', 'curl', 'astra-sm', 'dvbsnoop', 'ffmpeg', 'duktape', 'gstplayer', 'exteplayer3', 'enigma2-plugin-systemplugins-serviceapp', 'enigma2-plugin-extensions-epgimport', 'gstreamer1.0-plugins-good',
                        'gstreamer1.0-plugins-base', 'gstreamer1.0-plugins-ugly', 'libgstplayer-1.0-0', 'python-requests', 'python-sqlite3', 'python-codecs', 'python-core', 'python-json', 'python-netclient', 'python-image']
        if version_info[0] == 3:
            self.package = list(
                map(lambda x: x.replace('python', 'python3').replace('python3-imaging', 'python3-pillow'), self.package))

    def banner(self):
        system('clear')
        print(B, r'''
        888888 oP"Yb. .dP"Y8  dP""b8 88""Yb 88 88""Yb 888888
        88__   "' dP' `Ybo." dP   `" 88__dP 88 88__dP   88
        88""     dP'  o.`Y8b Yb      88"Yb  88 88"""    88
        888888 .d8888 8bodP'  YboodP 88  Yb 88 88       88''', C)

    def Stb_Image(self):
        if isfile('/etc/opkg/opkg.conf'):
            self.status = '/var/lib/opkg/status'
            self.update = 'opkg update >/dev/null 2>&1'
            self.install = 'opkg install'
        else:
            self.status = '/var/lib/dpkg/status'
            self.update = 'apt-get update >/dev/null 2>&1'
            self.install = 'apt-get install'
        return isfile('/etc/opkg/opkg.conf')

    def package_check(self, pkg):
        with open(self.status) as file:
            for item in file.readlines():
                if item.startswith('Package:'):
                    if findall(pkg, item[item.index(' '):].strip(), MULTILINE):
                        return True
            file.close()

    def distro(self):
        try:
            if isfile('/etc/issue'):
                self.image = open("/etc/issue").readlines()[-2].strip()[:-6]
                return self.image.capitalize().replace("develop", "Nightly Build")
            elif isfile('/usr/lib/enigma.info'):
                self.image = open('/usr/lib/enigma.info').readlines()
                for file_name in self.image:
                    if match('distro', file_name):
                        return file_name.split('=')[-1].strip().capitalize()
        except:
            return 'undefined'

    def password_check(self):
        check = popen("passwd -S | awk '{print$2}'").read().strip()
        if check == 'NP':
            print("{}(!){} Please Enter {}Password{} For {}{}{} : ".format(
                R, C, Y, C, B, self.distro(), C), end='')
            root = input()
            system("".join(["echo 'root:", root, "' | chpasswd"]))

    def get_info(self, item):
        try:
            req = Request("".join([self.URL, 'e2script.json']))
            req.add_header(
                'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0')
            response = urlopen(req)
            return loads(response.read()).get(item)
        except HTTPError as e:
            print('HTTP Error code: ', e.code)
        except URLError as e:
            print('URL Error: ', e.reason)

    def prompt(self, choices):

        options = list(choices)
        options.sort(key=int)
        while True:
            print(
                "{}(?){} Choose an option [{}-{}] : ".format(B, C, options[0], options[-1]), end='')
            choice = [str(x) for x in input().split()]

            for name in choice:
                if name not in options:
                    print(
                        "\n{}(!){} Select one of the available options !!\n".format(R, C))
                    continue
            return choice

    def delete(self):
        print('{}(?){} Now It Will be deleted Old Settings And Add The New'.format(B, C))

        for file in ['lamedb', '*list', '*.tv', '*.radio', 'satellites.xml']:
            if file != 'satellites.xml':
                self.path_dir = '/etc/enigma2/'
            else:
                self.path_dir = '/etc/tuxbox/'
            if isfile(join(self.path_dir, file)):
                remove(join(self.path_dir, file))

        sleep(0.8)
        urlretrieve('http://127.0.0.1/web/servicelistreload?mode=0')

    def channel(self, fname):
        url_settings = 'http://178.63.156.75/paneladdons/'
        chdir('/tmp')

        if isfile(fname):
            remove(fname)

        if fname == 'ciefp-e2-settings-75e-34w.tar.gz':
            link_settings = "".join([url_settings, "Ciefp/"])
        elif fname == 'vhannibal-settings-e2-motor-70e-45w.tar.gz':
            link_settings = "".join([url_settings, "Vhannibal/"])
        elif fname == 'GioppyGio_E2_Motor_75E-45W.tar.gz':
            link_settings = "".join([url_settings, "GioppyGio/"])
        elif fname == 'predrag-settings-e2-motor-42e-30w.tar.gz':
            link_settings = "".join([url_settings, "Predr@g/"])

        print("{}Downloading{} And Installing Channel {}Please Wait{} {}......{}".format(
            Y, C, R, C, G, C))

        urlretrieve("".join([link_settings, fname]), filename=fname)

        sleep(0.8)
        self.delete()
        sleep(0.8)

        with TarFile.open(fname) as tar_ref:
            for member in tar_ref.getmembers():
                tar_ref.extract(member, "/")
        tar_ref.close()

        if isfile(fname):
            remove(fname)

        sleep(0.8)
        print('{}(?){} Reload UserBouquets and LameDB'.format(B, C))
        urlretrieve('http://127.0.0.1/web/servicelistreload?mode=0')
        sleep(0.8)

        print(''.join(['Channel ', fname.split('.')[0], ' Installed']))

    def Main_Menu(self):

        print("\n{}(?){} Choose the Plugin Install:".format(B, C))

        menu = """
                                (00) Exit       (0) Default

        (1) AjPanel         (10) SubsSupport         (19) DreamSatPanel      (28) RakutenTV
        (2) Quran           (11) NewVirtualKeyBoard  (20) JediMakerXtream    (29) ChocholousekPicons
        (3) RaedQuickSignal (12) Suptv               (21) Xstreamity         (30) OpenWebif Only DreamOS
        (4) ArabicSavior    (13) IPtoSAT             (22) XcPlugin Forever   (31) NovaCam
        (5) YouTube         (14) EPG Grabber         (23) OpenMultiboot      (32) NovalerTV
        (6) KeyAdder        (15) EMU Install         (24) AthanTimes
        (7) E2IPLAYER       (16) PlutoTV             (25) BackupFlash
        (8) FootOnsat       (17) FlashOnline         (26) FreeServerCCcam
        (9) IPAudioPlus     (18) XtraEvent           (27) HasBahCa
        """

        channel = """
        (40) ciefp Motor  68°E-30°W     (43) Predr@g Motor 42°E-30°W
        (41) Vhannibal Motor 70°E-45°W  (44) MOHAMED Motor 52°E-30°W
        (42) GioppyGio Motor 75°E-45°W"""

        print(menu, '\n', channel, '\n')

    def check_prompt(self):
        self.cam = {"00": exit,
                    "0": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
                    "1": self.get_info('ajpanel'),
                    "2": self.get_info('quran'),
                    "3": self.get_info('raedquicksignal'),
                    "4": self.get_info('arabic_savior'),
                    "5": self.get_info('youtube'),
                    "6": self.get_info('keyadder'),
                    "7": self.get_info('e2iplayer'),
                    "8": self.get_info('footonsat'),
                    "9": self.get_info('novaipaudio'),
                    "10": self.get_info('subssupport'),
                    "11": self.get_info('newvirtualkeyBoard'),
                    "12": self.get_info('suptv'),
                    "13": self.get_info('iptosat'),
                    "14": self.get_info('epg_grabber'),
                    "15": self.get_info('emu'),
                    "16": self.get_info('pluto'),
                    "17": self.get_info('flashonline'),
                    "18": self.get_info('xtraevante'),
                    "19": self.get_info('dreamsatpanel'),
                    "20": self.get_info('jedimakerxtream'),
                    "21": self.get_info('xstreamity'),
                    "22": self.get_info('xc_code'),
                    "23": self.get_info('openmultiboot'),
                    "24": self.get_info('athantimes'),
                    "25": self.get_info('backupflash'),
                    "26": self.get_info('freeserver'),
                    "27": self.get_info('hasbahca'),
                    "28": self.get_info('rakutentv'),
                    "29": self.get_info('chocholousekpicons'),
                    "30": self.get_info('openwebif'),
                    "31": self.get_info('novacam'),
                    "32": self.get_info('novalertv'),
                    "40": "ciefp-e2-settings-75e-34w.tar.gz",
                    "41": "vhannibal-settings-e2-motor-70e-45w.tar.gz",
                    "42": "GioppyGio_E2_Motor_75E-45W.tar.gz",
                    "43": "predrag-settings-e2-motor-42e-30w.tar.gz",
                    "44": self.get_info('channel_os')}

        self.Main_Menu()

        for name in self.prompt(self.cam.keys()):
            if name == '00':
                print("GoodBye ...!\n", "   Written by {}MOHAMED_OS{}(͡๏̯͡๏) \n".format(
                    B, C, R, C))
                exit()
            elif name == '0':
                self.list_pkg.extend(self.cam.get(name))

                if not self.hostname in ['novaler4k', 'novaler4kse', 'multibox', 'multiboxse']:
                    self.list_pkg.remove('9')

            else:
                self.list_pkg.append(name)

    def FixFootONsat(self):
        target = "dif = int(timezone.replace('+', '').replace('00', ''))","dif = int(timezone.replace('-', '').replace('00', ''))"
        src = "dif = int(timezone.replace('+', '-').replace('00', ''))", "dif = int(timezone.replace('00', ''))"

        with open('/usr/lib/enigma2/python/Plugins/Extensions/FootOnSat/ui/interface.py', 'r+') as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            f.write(content.replace(target[0], src[0]).replace(target[1], src[1]))

    def main(self):
        self.Stb_Image()

        self.banner()
        sleep(1)
        print("\n")

        self.password_check()
        sleep(1)

        print("\n{}(!){} Please Wait Check Package ...".format(R, C))
        system(self.update)
        sleep(1)

        for filename in self.package:
            if not self.package_check(filename):
                system('clear')
                print("     Need To InsTall : {}{}{}\n".format(Y, filename, C))
                system(" ".join([self.install, filename]))
                sleep(1)

        system('clear')
        self.banner()

        self.check_prompt()
        numbers = list(dict.fromkeys(self.list_pkg))
        numbers.sort(key=int)
        for name in numbers:

            if name in ['40', '41', '42', '43']:
                self.channel(self.cam.get(name))
            else:
                system(self.cam.get(name))
                sleep(5)

            if name == '8':
                self.FixFootONsat()

        print('{}(?){} Device will restart now'.format(B, C))
        if self.Stb_Image():
            system('killall -9 enigma2')
        else:
            system('systemctl restart enigma2')


if __name__ == '__main__':
    build = Script()
    build.main()
