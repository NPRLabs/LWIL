import clock_array
import csv
import datetime
#import importlib
import os
import re
import shutil
import subprocess
import sys

def loudnessTest(show, dayo = 0):

	dayo = int(dayo)
	print "DAY"
	print dayo
	print "DAY"
	curPath = os.getcwd()
	curPath = '/Users/username/Desktop/Loudness'
	
	log = open(curPath + '/full.txt', 'w')
	elog = open(curPath + '/er_log.txt', 'w')

	stdout = log
	stderr = log

	command = 'mount_smbfs //username:pw.pw.@ad.npr.org/news /Users/username/news/'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)

	command = 'rm '+curPath+'/wav/*.wav'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)

	command = 'rm '+curPath+'/png/*'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)



	with open(curPath + '/calls.csv', 'rb') as csvfile:
		a = csv.reader(csvfile)
		for row in a:
			if (show == row[0]):
				name = row[1]
				#num = int(row[2])
				clock_len = int(row[3])
				hrs = int(row[4])
				start = int(row[5])
				eo = int(row[6])
				#dayo = int(row[7])
				#segs = row[8]
				offset = int(row[9])
				head = row[10]
			else:
				print "else"
		print "Show = " + show + str(start) + " + " + str(clock_len)
	yday = (datetime.date.today() - datetime.timedelta(days=dayo)).strftime("%m-%d")
	
	copyanalyze(name,hrs,curPath,yday,start,eo)
	
	clearup(curPath)
	remove(curPath)
	
#	command = 'diskutil unmount /Users/username/news/'
	#c = subprocess.call(command, stdout=log, stderr=log, shell=True)
#	print "unmount"
	
	rearrange(curPath,name,hrs,clock_len,offset)
	
	svgcreate(curPath,hrs,name,head,dayo)
	
def copyanalyze(name,hrs,curPath,yday,start,eo):
	log = open(curPath + '/full.txt', 'w')
	elog = open(curPath + '/er_log.txt', 'w')

	stdout = log
	stderr = log

	if name == "ME":
		from clock_array import me_clock
		clock = me_clock
	elif name == "ATC":
		from clock_array import atc_clock
		clock = atc_clock
	else:
		from clock_array import we_clock
		clock = we_clock	
	
	for j in range (0,hrs):
		if ((start+j+eo) % 2) == 0:
			m = str(1)
		else:
			m = str(4)
		if (start + j) > 9:
			n = ""
			print "n = " + str(n)
		else:
			n = "0"
			print "n = " + str(n)

		command = 'cp /Users/username/news/DC-Production/Media/Recordings/Rollovers/MultiCoder_SOAP_'+m+'_DCTECH-MC01X_'+ yday +'-2017_'+str(n)+str(start+j)+'-00-00.wav '+curPath+'/wav/MultiCoder_SOAP_'+m+'_DCTECH-MC01X_'+ yday +'-2017_'+n+str(start+j)+'-00-00.wav'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)
		print command
		
	command = 'chmod 777 '+curPath+'/wav/*.wav'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	for j in range (0,hrs):
		if ((start+j+eo) % 2) == 0:
			m = str(1)
		else:
			m = str(4)
		if (start + j) > 9:
			n = ""
		else:
			n = "0"
		command = curPath + '/bin/ffmpeg -nostats -i '+curPath+'/wav/MultiCoder_SOAP_'+m+'_DCTECH-MC01X_'+ yday +'-2017_'+str(n)+str(start+j)+'-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)
		print type(n)
		print n
		
	num_segments = len(clock)
	for k in range (0,hrs):
		for j in range(0,num_segments):
			if ((start+k+eo) % 2) == 0:
				m = str(1)
			else:
				m = str(4)
			print m

			if (start + k) > 9:
				n = ""
			else:
				n = "0"
			command = curPath + '/bin/ffmpeg -i '+ curPath+'/wav/MultiCoder_SOAP_'+m+'_DCTECH-MC01X_'+ yday +'-2017_' + n + str(start+k)+'-00-00.wav -acodec copy -to '\
				 + clock[j][2] + ' -ss ' + clock[j][1] + " " + curPath+ '/wav/' + clock[j][0] + '_' + 'MultiCoder_SOAP_'+m+'_DCTECH-MC01X_'+ yday +'-2017_'+n+str(start+k)+'-00-00.wav'				
			c = subprocess.call(command, stdout=log, stderr=log, shell=True)
			command = curPath + '/bin/ffmpeg -nostats -i ' + curPath + '/wav/' + clock[j][0] + '_' + 'MultiCoder_SOAP_'+m+'_DCTECH-MC01X_'+ yday +'-2017_'+n+str(start+k)+'-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
			c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	#log.close()
	log.close()
	elog.close()
	


def openlogs(curPath):
	log = open(curPath + '/full.txt', 'w')
	elog = open(curPath + '/er_log.txt', 'w')

	stdout = log
	stderr = log

def closelogs(path):
	path.close()

def clearup(curPath):
	#log = open(curPath + '/full.txt', 'w')
	#elog = open(curPath + '/ME_log.txt', 'w')

	#stdout = log
	#stderr = log
	
	infile = curPath + "/full.txt"
	outfile = curPath + "/two.txt"
	finfile = curPath + "/three.txt"
	cleanfile = curPath + "/four.txt"

	delete_list = ["ffmpeg version N-73361-g03b2b40 Copyright (c) 2000-2015 the ffmpeg developers","Output #0, null, to 'pipe:", "  built with gcc 4.9.2 (GCC)", "  configuration: --disable-static --enable-shared --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libdcadec --enable-libfreetype --enable-libgme --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-lzma --enable-decklink --enable-zlib", "  libavutil      54. 27.100 / 54. 27.100", "  libavcodec     56. 46.100 / 56. 46.100", "  libavformat    56. 40.100 / 56. 40.100", "  libavdevice    56.  4.100 / 56.  4.100", "  libavfilter     5. 19.100 /  5. 19.100", "  libswscale      3.  1.101 /  3.  1.101", "  libswresample   1.  2.100 /  1.  2.100", "  libpostproc    53.  3.100 / 53.  3.100", "Guessed Channel Layout for  Input Stream #0.0 : stereo", "Input #0, wav, from '", "':", "  Metadata:", "    comment         : ", "    date            : ", "    encoder         : Lavf56.40.100", "  Duration: ", "  , bitrate: 1536 kb/s", "    Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 48000 Hz, 2 channels, s16, 1536 kb/s", "Output #0, null, to 'pipe:':", "  Metadata:", "    comment         : ", "    date            : ", "    encoder         : Lavf56.40.100", "    Stream #0:0: Audio: pcm_s16le, 48000 Hz, stereo, s16, 1536 kb/s", "    Metadata:", "      encoder         : Lavc56.46.100 pcm_s16le", "Stream mapping:", "  Stream #0:0 (pcm_s16le) -> ebur128", "  ebur128 -> Stream #0:0 (pcm_s16le)", "Press [q] to stop, [?] for help", "size=N/A time=", " bitrate=N/A    ", "video:0kB audio:", " subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown", "[Parsed_ebur128_0 @ 0000000000574900] Summary:", "", "  Integrated loudness:", "  Loudness range:", "  True peak:"]
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
	#["dBFS","dBFS\n"]]
	#,[",,,,,","*"]]
	#,[",,,,","$"],[",,,","%"],[",,","&&"]]
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



	#command = 'rm *.wav'
	#c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	#command = 'rm *.txt'
	#c = subprocess.call(command, stdout=log, stderr=log, shell=True)

def remove(curPath):
	shutil.copyfile(curPath + "/three.txt", curPath + "/three.csv")


	file_name = curPath + "/three.csv"

	buffered = open(file_name, 'rU').read()
	#print type(buffered)

	words = re.sub('dBFS,','dBFS\n',buffered)


	words = re.sub('ffmpeg version(.)*Loudness/','',words)

	words = re.sub("originator_reference: (.)*'Loudness/","",words)
	words = re.sub('originator_reference:(.)*Loudness/','',words)
	words = re.sub('encoder(.)*Summary:','',words)
	words = re.sub('\[null (.)*\]','',words)
	words = re.sub('Using (.)* instead.','',words)
	words = re.sub('-70.0(.)*-inf dBFS','',words)
	words = re.sub('originator_reference(.)*Summary:','',words)
	#words = re.sub(' LUFS,,,    Peak:       ','',words)
	words = re.sub('\[Parsed(.)*Summary:','',words)
	#words = re.sub('LUFS,(.)*LRA:','',words)
	words = re.sub('\s*,',',',words)
	words = re.sub(',\s*',',',words)
	words = re.sub('originator_reference(.)*I:','I:',words)
	words = re.sub(',,',',',words)
	words = re.sub(',,',',',words)
	words = re.sub('dBFS\n','\n',words)
	words = re.sub(',I:\s',',',words)
	words = re.sub(' LUFS(.)*LRA:(\s)*',',',words)
	words = re.sub('LU(.)*Peak:(\s)*',',',words)
	words = re.sub(',I:(.)*,        ',',',words)
	words = re.sub(',2017-..-..,',',',words)


	out_file = curPath + "/four.csv"
	output = open(out_file, 'w')
	output.write(words)

##rearrange
def rearrange(curPath,name,hrs,clock_len,offset):
	
	log = open(curPath + '/rearrange.csv', 'w')
	stdout = log
	stderr = log
	f = open(curPath + '/four.csv', 'rb')

	lucsv = csv.reader(f)
	lucsv = list(lucsv)
#	text = lucsv[1][2]


	if name == "ME":
		from segments import me
		segs = me
	elif name == "ATC":
		from segments import atc
		segs = atc
	else:
		from segments import we
		segs = we
	fill = lucsv[0][2]
	for j in range (1,hrs):
		#fill = lucsv[j][2]+","+fill
		fill = fill + "," + lucsv[j][2]
		print "1st" + str(j) + ":: " + fill
		print type(fill)
	log.write(str(segs[0])+","+fill+"\n")
		

	for i in range (0,clock_len):#r
		fill = lucsv[hrs+i][2]
		for j in range (1,hrs):#c
#			fill = lucsv[hrs*j+hrs+i][2]+","+fill
			fill = fill + "," + lucsv[clock_len*j+hrs+i][2]
			print str(j) + ":: " + fill
		log.write(str(segs[i+1])+","+fill+"\n")
		
##create
def svgcreate(curPath,hrs,name,head,dayo):
	errLog = curPath+'/er_log.txt'
	print errLog
	elog = open(errLog, 'w')

	command = 'mount_smbfs //username:g0ldfarbpw@dc-nprconnect/Divisions/eit/AEHelp/Procedures /Users/username/Procedures/'
	c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)


	if name == "ME":
		from segments import me, meHrs
		hours = meHrs
		cur = me
	elif name == "ATC":
		from segments import atc, atcHrs
		hours = atcHrs
		cur = atc
	elif name == "WATC":
		from segments import we, watcHrs
		hours = watcHrs
		cur = we
	else:
		from segments import we, weHrs
		hours = weHrs
		cur = we	

	for j in range(0,hrs):
		print j

		sName = name+'_'+str((datetime.date.today() - datetime.timedelta(days=dayo)).strftime("%a")) +"_"+ hours[j]
		fileName = curPath+'/svg/'+sName+'.svg'
		print fileName

		log = open(fileName, 'w')
		stdout = log
		stderr = log

		with open(curPath+'/'+head+'.txt','rU') as header:
			headerText = header.read()
			#.replace('\n','')

		log.write(headerText+"\n\n")

		with open(curPath+'/rearrange.csv', 'rb') as csvfile:
			wo = csv.reader(csvfile, delimiter=',', quotechar='"')
			i = 0
			print j
			print i
			for row in wo:
				print "i: " + str(i) + " \ j: " + str(j)
				#print row[1+j]
				if row[1+j] < -28.5:
					print type(val)
					print type(row[1+j])
					val = -28.5
				else:
					val = (float(row[1+j])+28.5)*100
				if (float(row[1+j]) == -70):
					color = ""
				elif ((float(row[1+j])<-26) or (float(row[1+j])>-22)):
					color = 'font-weight: bold; fill:red;'
				elif ((float(row[1+j])<-25) or (float(row[1+j])>-23)):
					color = 'fill:	red;'
				else:
					color = ""
				print color
				if (float(row[1+j]) == -70):
					pval = ""
				else:
					pval = str('{:.1f}'.format(float(row[1+j])))
				log.write('<text x="210" y="'+str(50+i*25)+'" style="text-anchor: end;'+color+'">'+cur[i]+'  ['+pval+']'+'</text>\n\t<rect x="250" y="'+str(40+25*i)+'" width="'+str(val)+'" height="15" fill="steelblue"></rect>\n')
				i = i + 1

		log.write('</g>\n<g>\n	<text x="20" y="40" style="font-size:40;">'+(datetime.date.today() - datetime.timedelta(days=dayo)).strftime("%a %b %d")+'</text>\n	<text x="20" y="80" style="font-size:20;">'+hours[j]+'</text>\n</g>\n</svg>')

		log.close()

		#command = 'qlmanage -t -s 1000 -o '+curPath+'/png/ '+fileName
		#c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)

		command = 'cp '+fileName+' /Users/username/Desktop/Loudness/svg/'+sName+'.svg'
		c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)
		print command
		
		"""command = 'mv svg/*.svg ../../../username/Procedures/Loudness/svg/'
		c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)
		print command
		"""

		#command = 'mv '+curPath+'/png/'+sName+'.svg'+'.png '+curPath +'/png/'+sName+'.png'
		#c = subprocess.call(command, stdout=elog, stderr=elog, shell=True)
		



if __name__ == '__main__':
    loudnessTest(*sys.argv[1:])