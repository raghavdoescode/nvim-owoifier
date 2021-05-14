import pynvim 

@pynvim.plugin
class Plugin(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command("OWOify")
    def owoify(self):
        file_path = self.vim.current.buffer.name
        with open(file_path, 'r+') as file:
            data = file.readlines()
            finaltext = ''

            for i in range(0, len(data)):
                for char in data[i]:
                    if char == 'R':
                        finaltext = finaltext + 'W'
                    elif char == 'r':
                        finaltext = finaltext + 'w'
                    elif char == 'L':
                        finaltext = finaltext + 'W'
                    elif char == 'l':
                        finaltext = finaltext + 'w'
                    else:
                        finaltext = finaltext + char
            file.seek(0) 
            file.truncate() 
            file.write(finaltext)
            file.close()
