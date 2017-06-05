
import csv
import datetime
import os
import re
import shutil
import subprocess
import sys

def loudnessTest():

	from segments import NewscastHrs

	curPath = os.getcwd()
	curPath = '/Users/agoldfarb/Desktop/Loudness'

	log = open(curPath + '/full.txt', 'w')
	stdout = log
	stderr = log

	elog = open(curPath + '/NC_log.txt', 'w')
	
	getVals(elog,log,curPath)
	clearup(curPath)

	command = 'diskutil unmount /Users/agoldfarb/news/'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)

	createsvg(curPath,NewscastHrs)

def getVals(elog,log,curPath):
	command = 'mount_smbfs //agoldfarb:jam3s.jam3s.@ad.npr.org/news /Users/agoldfarb/news/'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)

	yday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%m-%d")

	command = 'rm '+curPath+'/*.wav'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)


	command = 'rm '+curPath+'/png/*'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)


	for i in range (0,10):
		print i

		command = 'cp /Users/agoldfarb/news/DC-Production/Media/Recordings/Rollovers/MultiCoder_SOAP_3_DCTECH-MC01X_'+ yday +'-2017_0'+str(i)+'-01-00.wav '+curPath+'/wav/MultiCoder_SOAP_3_DCTECH-MC01X_'+ yday +'-2017_0'+str(i)+'-01-00.wav'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	for i in range (10,24):
		print i

		command = 'cp /Users/agoldfarb/news/DC-Production/Media/Recordings/Rollovers/MultiCoder_SOAP_3_DCTECH-MC01X_'+ yday +'-2017_'+str(i)+'-01-00.wav '+curPath+'/wav/MultiCoder_SOAP_3_DCTECH-MC01X_'+ yday +'-2017_'+str(i)+'-01-00.wav'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'chmod 777 '+curPath+'/wav/*.wav'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)

	for i in range (0,10):

		command = curPath+'/bin/ffmpeg -nostats -i '+curPath+'/wav/MultiCoder_SOAP_3_DCTECH-MC01X_'+ yday +'-2017_0'+str(i)+'-01-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	for i in range (10,24):

		command = curPath+'/bin/ffmpeg -nostats -i '+curPath+'/wav/MultiCoder_SOAP_3_DCTECH-MC01X_'+ yday +'-2017_'+str(i)+'-01-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)




def clearup(curPath):
	infile = curPath + '/full.txt'
	outfile = curPath + '/two.txt'
	finfile = curPath + '/three.txt'
	cleanfile = curPath + '/four.txt'

	delete_list = ["ffmpeg version N-79995-ge7a9b43-tessus Copyright (c) 2000-2017 the FFmpeg developers","built with Apple LLVM version 6.0 (clang-600.0.57) (based on LLVM 3.5svn)","configuration:--cc=/usr/bin/clang --prefix=/opt/","","[null @ 0x7f8b61801c00] Using AVStream.codec to pass codec parameters to muxers is deprecated, use AVStream.codecpar instead.","Output #0, null, to 'pipe:", "  built with gcc 4.9.2 (GCC)", "  configuration: --disable-static --enable-shared --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libdcadec --enable-libfreetype --enable-libgme --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-lzma --enable-decklink --enable-zlib", "  libavutil      54. 27.100 / 54. 27.100", "  libavcodec     56. 46.100 / 56. 46.100", "  libavformat    56. 40.100 / 56. 40.100", "  libavdevice    56.  4.100 / 56.  4.100", "  libavfilter     5. 19.100 /  5. 19.100", "  libswscale      3.  1.101 /  3.  1.101", "  libswresample   1.  2.100 /  1.  2.100", "  libpostproc    53.  3.100 / 53.  3.100", "Guessed Channel Layout for  Input Stream #0.0 : stereo", "Input #0, wav, from '", "':", "  Metadata:", "    comment         : ", "    date            : ", "    encoder         : Lavf56.40.100", "  Duration: ", "  , bitrate: 1536 kb/s", "    Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 48000 Hz, 2 channels, s16, 1536 kb/s", "Output #0, null, to 'pipe:':", "  Metadata:", "    comment         : ", "    date            : ", "    encoder         : Lavf56.40.100", "    Stream #0:0: Audio: pcm_s16le, 48000 Hz, stereo, s16, 1536 kb/s", "    Metadata:", "      encoder         : Lavc56.46.100 pcm_s16le", "Stream mapping:", "  Stream #0:0 (pcm_s16le) -> ebur128", "  ebur128 -> Stream #0:0 (pcm_s16le)", "Press [q] to stop, [?] for help", "size=N/A time=", " bitrate=N/A    ", "video:0kB audio:", " subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown", "[Parsed_ebur128_0 @ 0000000000574900] Summary:", "", "  Integrated loudness:", "  Loudness range:", "  True peak:"]
	fin = open(infile)
	fout = open(outfile, "w+")

	for line in fin:
		for word in delete_list:
			line = line.replace(word, "")
		fout.write(line)

	fin.close()

	fout.close()

	cleanup_list = ["\n","\r"]
	fin = open(outfile)
	fout = open(finfile, "w+")

	for line in fin:
		for word in cleanup_list:
			line = line.replace(word, ",")
		fout.write(line)
	fin.close()
	fout.close()

	last_list = [["Threshold","*"]]
	fin = open(finfile)
	fout = open(cleanfile, "w+")

	for word in last_list:
		for string in finfile:
			print word[0]
			print word[1]
			string = string.replace(',','')
			fout.write(string)
	fin.close()
	fout.close()



	###
	shutil.copyfile(curPath+"/three.txt", curPath+"/three.csv")


	file_name = curPath + "/three.csv"

	buffered = open(file_name, 'rU').read()
	words = re.sub('dBFS,','dBFS\n',buffered)

	words = re.sub('Using AVStream(.)*codecpar instead','',words)
	print words

	words = re.sub('-cc=/usr/bin/clang --prefix=/opt/','',words)
	print words

	words = re.sub('-70(.)*-inf','',words)
	print words

	words = re.sub('\[null (.)*\]','',words)
	print words

	words = re.sub('configuration:','',words)
	words = re.sub(',,',',',words)
	words = re.sub(',,',',',words)
	words = re.sub(',,',',',words)
	words = re.sub(',,',',',words)
	words = re.sub(',,',',',words)

	words = re.sub(',,',',',words)

	words = re.sub(',,',',',words)

	words = re.sub(',,',',',words)

	words = re.sub(',,',',',words)

	words = re.sub(',,',',',words)

	words = re.sub('\n,','\n',words)
	#print words

	words = re.sub(',   -ffmpeg(.)*Multi','Multi',words)
	words = re.sub('originator_reference(.)*Summary:,    I:          dBFS','',words)
	words = re.sub(',(\s)*Summary(.)*I:(\s)*',',',words)

	words = re.sub('\n(\s)*','\n',words)
	words = re.sub('rm:(.)*MultiCoder','MultiCoder',words)

	words = re.sub('(\s)*LUFS(.)*LRA:(\s)*',',',words)
	words = re.sub('(\s)*LU(.)*Peak:(\s)*',',',words)
	words = re.sub(' dBFS\n','\n',words)
	words = re.sub('(.)*Multi','Multi',words)
	#
	#

	out_file = curPath + "/four.csv"
	output = open(out_file, 'w')
	output.write(words)



####

def createsvg(curPath,NewscastHrs):

	wkday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%a")
	print wkday
	sName = wkday+'_NC'
	fileName = curPath+'/'+sName+'.svg'
	print fileName

	log = open(fileName, 'w')
	stdout = log
	stderr = log

	elog = open(curPath + '/NC_log.txt', 'w')



	#	fileName = 'ATC_'+NewscastHrs[j]+'.svg'
	#	print fileName

	with open(curPath+'/headNC.txt','rU') as header:
		headerText = header.read()
			#.replace('\n','')

		log.write(headerText+"\n\n")

		with open(curPath+'/four.csv', 'rb') as csvfile:
			wo = csv.reader(csvfile, delimiter=',', quotechar='"')
			i = 0
			#print j
			print i
			for row in wo:
				print row[1]+row[2]
				if row[2] < -28.5:
					val = -28.5
				else:
					val = (float(row[2])+28.5)*50
				if (float(row[2]) == -70):
					color = ""
				elif ((float(row[2])<-26) or (float(row[2])>-22)):
					color = 'font-weight: bold; fill:red;'
				elif ((float(row[2])<-25) or (float(row[2])>-23)):
					color = 'fill:	red;'
				else:
					color = ""
				print color
				if (float(row[2]) == -70):
					pval = ""
				else:
					pval = str('{:.1f}'.format(float(row[2])))
				log.write('<text x="210" y="'+str(50+i*25)+'" style="text-anchor: end;'+color+'">'+NewscastHrs[i]+'  ['+pval+']'+'</text>\n\t<rect x="250" y="'+str(40+25*i)+'" width="'+str(val)+'" height="15" fill="steelblue"></rect>\n')
				i = i + 1

	#	log.write('</g>\n<g>\n	<text x="210" y="40" style="font-size:40;">'+(datetime.date.today() - datetime.timedelta(days=1)).strftime("%a %b %d")+'</text>\n	<text x="20" y="80" style="font-size:20;">'+NewscastHrs[j]+'</text>\n</g>\n</svg>')
		log.write('</g>\n</svg>')

		log.close()

		command = 'qlmanage -t -s 1000 -o '+curPath+'/ '+fileName
		c = subprocess.call(command, shell=True)
		
		command = 'cp '+fileName+' /Users/agoldfarb/Production/Loudness/svg/'+sName+'.svg'
		c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)
		print command

		command = 'mv '+fileName+'.png '+curPath+'/png/'+sName+'.png'
		c = subprocess.call(command, shell=True)


if __name__ == '__main__':
    loudnessTest(*sys.argv[1:])