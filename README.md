RetroGamez for XBMC (AdvancedLauncher Preset)
=============================================

* Author:    Kbalist (<lord_of_Kbal@hotmail.com>)
* Date:      July, 2011
* Last mod.: July, 2011
* Version:   0.0.1
* Website:   
* GitHub:    <https://github.com/kbalist/xbmc-games>


First of all thanks to : 

* xbmc
* http://www.iconspedia.com/pack/all-console-143/30.html


This free fileset is copyleft licensed under the same terms as Python, or,
at your option, under version 2 of the GPL license.

(The original script was written by reddit user [iwakun](http://www.reddit.com/user/iwakun).
See the `original_by_iwakun/` folder for more information.)

The goal of the script is to download images from a reddit category and 
create an XML file that can be set as background in Gnome. The XML file
will rotate the images.

Here is the list of changes that I added to the original version:

  This way an already fetched image (either good or bad) won't be downloaded again.
* The script can set the produced XML as your wallpaper, you don't need to
  do that manually. Also, XML production can be switched off if you want to
  use a different wallpaper manager.

For installing lxml, please refer to [this entry][1], where the 
installation procedure is explained at the end of the post.

[1]: https://pythonadventures.wordpress.com/2011/04/04/write-xml-to-file/


Usage:
------

First, you might want to customize some settings in the `config.py` file.
The most important thing is the `PHOTO_DIR` directory, i.e. where to store
the downloaded images. Create this directory if it doesn't exist.
Then, simply launch the script:

    ./wallpaper_downloader.py
    
You can also add it to your crontab:

    $ crontab -e
    10 */2 * * * /absolute_path_to/wallpaper_downloader.py
    
Add the second line to the end of the crontab list. Here the script is 
called at every two hours (at 0h10, 2h10, etc.).

**New:**

I changed the default behaviour of the script. By default it doesn't
generate an XML output. I find it a better solution to use a dedicated
wallpaper manager for this task. Rotating the images with an XML is not 
very flexible, a wallpaper manager can provide a better experience.
To this end, I wrote a simple wallpaper rotator that does the job (see 
the file `wallpaper_rotator.py`).
If you still want the XML, set it in the config file.


Managing the downloaded wallpapers:
-----------------------------------

There are several ways to manage the downloaded images:

1. The **new** way is to use `wallpaper_rotator.py`. Just launch it in the
   background. It uses the same config file as the wallpaper 
   downloader.
2. The old way is to generate an XML and set it as your wallpaper.
   The downloader can do all that; for customizations see the config file.


Contributors:
-------------

* Nathan B, alias [ndbroadbent][2]
* Adrian Castillejos, alias [zioyero][3]

[2]: https://github.com/ndbroadbent
[3]: https://github.com/zioyero


Discussion:
-----------

Maybe I should remove the XML generator part from the downloader. After all, it's
"just" a downloader, so it should do just one thing. Since I made a wallpaper
changer, I don't use the XML any more. The new rotator script is preferred over
the XML, thus XML is sort of deprecated.


TODO:
-----

1. Add support to more wallpaper sites: <http://wallbase.cc>, <http://4walled.org/>.

2. Add support to other operating systems: Windows, Mac.
