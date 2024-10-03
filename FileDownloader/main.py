from file_downloader import download_file as download
import tkinter as tk

root = tk.Tk()
root.title("File Downloader")
root.geometry("500x200")

def buttoncall():
    url = urlInput.get()
    fname = filenameInput.get()
    print(f"url:{url}\nFilename:{fname}")
    download(url,fname)
    pass


# label enter url
urlLabel = tk.Label(root, text="URL")
#urlLabel.pack(padx=10,pady=10)
urlLabel.grid(row=0,column=0)



# url_entry
urlInput = tk.Entry(root)
#urlInput.pack(padx=10,pady=10)
urlInput.grid(row=0,column=1)

#label enter file name 
filenameLabel = tk.Label(root,text="FileName")
filenameLabel.grid(row=2,column=0)

# filename entry
filenameInput = tk.Entry(root)
filenameInput.grid(row=2,column=1)


#button
downloadButton = tk.Button(root, text="Download", command=buttoncall)
downloadButton.grid(row=3,column=1)



root.mainloop()
