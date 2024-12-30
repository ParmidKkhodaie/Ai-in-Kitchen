import speech_recognition as sr
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)
def turn_on_led():
    GPIO.output(led_pin, GPIO.HIGH)
    print("چراغ روشن شد")
def process_audio(command):
    if 'چراغ را روشن کن' in command:
        turn_on_led()
recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_off_led():
    GPIO.output(led_pin, GPIO.LOW)
    print("چراغ خاموش شد")
def process_audio(command):
    if 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def open_water_valve():
    print("شیر آب باز شد")
def process_audio(command):
    if 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def close_water_valve():
    print("شیر آب بسته شد")
def process_audio(command):
    if 'شیر آب را ببند' in command:
        close_water_valve()
    elif 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_on_gas():
    print("گاز روشن شد")
def turn_off_gas():
    print("گاز خاموش شد")
def process_audio(command):
    if 'گاز را روشن کن' in command:
        turn_on_gas()
    elif 'گاز را خاموش کن' in command:
        turn_off_gas()
    elif 'شیر آب را ببند' in command:
        close_water_valve()
    elif 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_off_gas():
    print("گاز خاموش شد")
def process_audio(command):
    if 'گاز را روشن کن' in command:
        turn_on_gas()
    elif 'گاز را خاموش کن' in command:
        turn_off_gas()
    elif 'شیر آب را ببند' in command:
        close_water_valve()
    elif 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_on_oven():
    print("فر روشن شد")
def turn_off_oven():
    print("فر خاموش شد")
def process_audio(command):
    if 'فر را روشن کن' in command:
        turn_on_oven()
    elif 'فر را خاموش کن' in command:
        turn_off_oven()
    elif 'گاز را روشن کن' in command:
        turn_on_gas()
    elif 'گاز را خاموش کن' in command:
        turn_off_gas()
    elif 'شیر آب را ببند' in command:
        close_water_valve()
    elif 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_off_oven():
    print("فر خاموش شد")
def process_audio(command):
    if 'فر را روشن کن' in command:
        turn_on_oven()
    elif 'فر را خاموش کن' in command:
        turn_off_oven()
    elif 'گاز را روشن کن' in command:
        turn_on_gas()
    elif 'گاز را خاموش کن' in command:
        turn_off_gas()
    elif 'شیر آب را ببند' in command:
        close_water_valve()
    elif 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_on_fridge():
    print("یخچال روشن شد")
def turn_off_fridge():
    print("یخچال خاموش شد")
def process_audio(command):
    if 'یخچال را روشن کن' in command:
        turn_on_fridge()
    elif 'یخچال را خاموش کن' in command:
        turn_off_fridge()
    elif 'فر را روشن کن' in command:
        turn_on_oven()
    elif 'فر را خاموش کن' in command:
        turn_off_oven()
    elif 'گاز را روشن کن' in command:
        turn_on_gas()
    elif 'گاز را خاموش کن' in command:
        turn_off_gas()
    elif 'شیر آب را ببند' in command:
        close_water_valve()
    elif 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_on_dishwasher():
    print("ماشین ظرفشویی روشن شد")
def process_audio(command):
    if 'ماشین ظرفشویی را روشن کن' in command:
        turn_on_dishwasher()
    elif 'یخچال را روشن کن' in command:
        turn_on_fridge()
    elif 'یخچال را خاموش کن' in command:
        turn_off_fridge()
    elif 'فر را روشن کن' in command:
        turn_on_oven()
    elif 'فر را خاموش کن' in command:
        turn_off_oven()
    elif 'گاز را روشن کن' in command:
        turn_on_gas()
    elif 'گاز را خاموش کن' in command:
        turn_off_gas()
    elif 'شیر آب را ببند' in command:
        close_water_valve()
    elif 'شیر آب را باز کن' in command:
        open_water_valve()
    elif 'چراغ را خاموش کن' in command:
        turn_off_led()
    elif 'چراغ را روشن کن' in command:
        turn_on_led()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_on_dishwasher():
    print("ماشین ظرفشویی روشن شد")
def process_audio(command):
    if 'ماشین ظرفشویی را روشن کن' in command:
        turn_on_dishwasher()
    elif 'ماشین ظرفشویی را خاموش کن' in command:
        turn_off_dishwasher()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_off_dishwasher():
    print("ماشین ظرفشویی خاموش شد")
def process_audio(command):
    if 'ماشین ظرفشویی را روشن کن' in command:
        turn_on_dishwasher()
    elif 'ماشین ظرفشویی را خاموش کن' in command:
        turn_off_dishwasher()
    else:
        print("دستور ناشناخته")
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_on_microwave():
    print("مایکروویو روشن شد")
def process_audio(command):
    if 'مایکروویو را روشن کن' in command:
        turn_on_microwave()
    else:
        print("دستور ناشناخته")
recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)
try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")
def turn_off_microwave():
    print("مایکروویو خاموش شد")
def process_audio(command):
    if 'مایکروویو را روشن کن' in command:
        turn_on_microwave()
    elif 'مایکروویو را خاموش کن' in command:
        turn_off_microwave()
    else:
        print("دستور ناشناخته")
recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    print("لطفا یک دستور وارد کنید:")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio, language="fa-IR")
    print("دستور نوشته شده: ", command)
    process_audio(command)
except sr.UnknownValueError:
    print("متوجه نشدم!")
except sr.RequestError:
    print("مشکل در برقراری ارتباط با Google Speech Recognition!")