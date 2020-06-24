import os

def main():
    indir = r'your input directory'
    outdir = r'your output directory'
    # Get all files in a folder
    infolder = os.listdir(indir)

    count = 0
    for infile in infolder:

        filename = infile[0:infile.find('.')]

        # A binary read of the file
        file = open(os.path.join(indir, infile), 'rb')
        infilebytes = file.read()
        newfile = []

        # find if the file is jpeg (0xFF and 0xD8) as the hex code is  FFD8 at the start of the file. XOR it.
        if (infilebytes[0] ^ 0xFF) == (infilebytes[1] ^ 0xD8):
            xorjpg = infilebytes[0] ^ 0xFF
            print('%s,file is JPG encrypted XOR: ' % (infile, xorjpg))

            # convert all bytes via the xor formula and spit out a new file
            for i in infilebytes:
                newbyte = i ^ xorjpg
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
            file2 = open(os.path.join(outdir, filename+'.jpg'), 'wb')
            file2.write(newfile2)
            count += 1

        # find if the file is PNG (0x89 and 0x50) as the hex code is  8950 at the start of the file. XOR it.
        elif (infilebytes[0] ^ 0x89) == (infilebytes[1] ^ 0x50):
            xorpng = infilebytes[0] ^ 0x89
            print('%s,file is PNG encrypted XOR: ' % (infile, xorpng))
            for i in infilebytes:
                newbyte = i ^ xorpng
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
            file2 = open(os.path.join(outdir, filename+'.png'), 'wb')
            file2.write(newfile2)
            count += 1

# find if the file is GIF (0x47 and 0x49) as the hex code is  4749 at the start of the file. XOR it.
        elif (infilebytes[0] ^ 0x47) == (infilebytes[1] ^ 0x49):
            xorgif = infilebytes[0] ^ 0x47
            print('%s,file is GIF encrypted XOR: ' % (infile, xorgif))
            for i in infilebytes:
                newbyte = i ^ xorgif
                newfile.append(newbyte)
            newfile2 = bytes(newfile)
            file2 = open(os.path.join(outdir, filename+'.gif'), 'wb')
            file2.write(newfile2)
            count += 1
        else:
            print('%s, file type is unrecognized！' % infile)
    print('identified %d images ' % count)

if __name__ == '__main__':
    main()
