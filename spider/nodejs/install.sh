#!/bin/bash
set -e
#初始化
os_name=`uname -s`
machine=`uname -m`
PWD_PATH=`pwd`
if grep -Eqi "CentOS" /etc/issue || grep -Eq "CentOS" /etc/*-release; then
    DISTRO='RHEL'
elif grep -Eqi "Red Hat Enterprise Linux Server" /etc/issue || grep -Eq "Red Hat Enterprise Linux Server" /etc/*-release; then
    DISTRO='RHEL'
elif grep -Eqi "Debian" /etc/issue || grep -Eq "Debian" /etc/*-release; then
    DISTRO='Debian'
elif grep -Eqi "Ubuntu" /etc/issue || grep -Eq "Ubuntu" /etc/*-release; then
    DISTRO='Debian'
else
    DISTRO='unknow'
fi
#chromium_verison 版本号
chromium_verison='599821'
chromium_dir=$PWD_PATH"/node_modules/puppeteer/.local-chromium"
if [[ "$DISTRO" == "RHEL" ]]; then
    #依赖库
	yum install pango.x86_64 libXcomposite.x86_64 libXcursor.x86_64 libXdamage.x86_64 libXext.x86_64 libXi.x86_64 libXtst.x86_64 cups-libs.x86_64 libXScrnSaver.x86_64 libXrandr.x86_64 GConf2.x86_64 alsa-lib.x86_64 atk.x86_64 gtk3.x86_64 wget -y
	#字体
	yum install ipa-gothic-fonts xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-utils xorg-x11-fonts-cyrillic xorg-x11-fonts-Type1 xorg-x11-fonts-misc -y
elif [[ "$DISTRO" == "Debian" ]]; then
    sudo apt install -f \
            gconf-service \
            libasound2 \
            libatk1.0-0 \
            libatk-bridge2.0-0 \
            libc6 \
            libcairo2 \
            libcups2 \
            libdbus-1-3 \
            libexpat1 \
            libfontconfig1 \
            libgcc1 \
            libgconf-2-4 \
            libgdk-pixbuf2.0-0 \
            libglib2.0-0 \
            libgtk-3-0 \
            libnspr4 \
            libpango-1.0-0 \
            libpangocairo-1.0-0 \
            libstdc++6 \
            libx11-6 \
            libx11-xcb1 \
            libxcb1 \
            libxcomposite1 \
            libxcursor1 \
            libxdamage1 \
            libxext6 \
            libxfixes3 \
            libxi6 \
            libxrandr2 \
            libxrender1 \
            libxss1 \
            libxtst6 \
            ca-certificates \
            fonts-liberation \
            libappindicator1 \
            libnss3 \
            lsb-release \
            xdg-utils \
            wget

fi
local_chromium_dir=${chromium_dir}"/linux-"${chromium_verison}"/"
if [[ "$os_name" == "Linux" ]]; then
    download_url="https://npm.taobao.org/mirrors/chromium-browser-snapshots/Linux_x64/${chromium_verison}/chrome-linux.zip"
elif [[ "$os_name" == "Darwin" ]]; then
    download_url="https://npm.taobao.org/mirrors/chromium-browser-snapshots/Mac/${chromium_verison}/chrome-mac.zip"
    local_chromium_dir=${chromium_dir}"/mac-"${chromium_verison}"/"
fi
read -p "是否需要自动下载Chromium (1,自动下载,2,手动下载)：" INPUT_STRING
case $INPUT_STRING in
	1)
		npm install --registry https://registry.npm.taobao.org
		;;
	2)
		echo "正在从 npm.taobao.org 下载 Chromium……"
		wget -O chrome.zip ${download_url}
		npm install  --ignore-scripts --registry https://registry.npm.taobao.org
		if [[ ! -d ${local_chromium_dir} ]]; then
            mkdir -p ${local_chromium_dir}
        fi
		unzip -d ${local_chromium_dir} chrome.zip
		rm chrome.zip
		;;
	*)
		echo "选择不正确"
		;;
esac
