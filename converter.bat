@echo off
cd %cd%/ui/
pyrcc5 main_resources.qrc -o main_resources_rc.py
pyuic5 -x main_interface.ui -o ui_mainInterface.py
pyuic5 -x login_form.ui -o ui_startInterface.py
echo Done!
pause