import speech_recognition as sr
washing_machine_on = False
gas_stove_on = False
kitchen_lights_on = False
water_valve_on = False
def get_audio(appliance):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("لطفاً صحبت کنید:")
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data, language="fa-IR")
            print("صدای شناسایی شده:", text)
            if appliance == "لباسشویی" and "لباسشویی روشن شود" in text:
                global washing_machine_on
                washing_machine_on = True
                print("لباسشویی روشن شد")
            elif appliance == "لباسشویی" and "لباسشویی خاموش شود" in text:
                global washing_machine_on
                washing_machine_on = False
                print("لباسشویی خاموش شد")
            elif appliance == "فرگاز" and "فرگاز روشن شود" in text:
                global gas_stove_on
                gas_stove_on = True
                print("فرگاز روشن شد")
            elif appliance == "فرگاز" and "فرگاز خاموش شود" in text:
                global gas_stove_on
                gas_stove_on = False
                print("فرگاز خاموش شد")
            elif appliance == "چراغ اشپزخانه" and "چراغ های اشپزخانه روشن شود" in text:
                global kitchen_lights_on
                kitchen_lights_on = True
                print("چراغ های اشپزخانه روشن شد")
            elif appliance == "چراغ اشپزخانه" and "چراغ های اشپزخانه خاموش شود" in text:
                global kitchen_lights_on
                kitchen_lights_on = False
                print("چراغ های اشپزخانه خاموش شد")
            elif appliance == "شیر آب" and "شیر آب باز شود" in text:
                global water_valve_on
                water_valve_on = True
                print("شیر آب باز شد")
            elif appliance == "شیر آب" and "شیر آب ببند شود" in text:
                global water_valve_on
                water_valve_on = False
                print("شیر آب بسته شد")
        except sr.UnknownValueError:
            print("صدای شناسایی نشد.")
        except sr.RequestError:
            print("خطایی رخ داد.")
while True:
    get_audio("لباسشویی")
    get_audio("فرگاز")
    get_audio("چراغ اشپزخانه")
    get_audio("شیر آب")