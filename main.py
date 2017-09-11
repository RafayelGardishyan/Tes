from Engine import Assistant
from Configuration import ConfigurationWindow as CW

if __name__ == '__main__':
    with open('Configuration/data/configured.log', 'r+') as f:
        if f.read() == 'false':
            cw = CW()
            cw = None
            f.close()
        else:
            pass
        f.close()

    app = Assistant()
    app.mainloop()