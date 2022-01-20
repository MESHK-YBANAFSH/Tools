from re import findall
from rubika.client import Bot
from requests import get
from rubika.encryption import encryption
from rubika.tools import Tools
import requests
import time

bot = Bot("uqmmhbnbbrbtxmdywafqqlxckiamgrkg")
target = "g0BTmU40d1022078181f16d8a3fe6cb5"

def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData

def hasAds(msg):
	links = list(map(lambda ID: ID.strip()[1:],findall("@[\w|_|\d]+", msg))) + list(map(lambda link:link.split("/")[-1],findall("rubika\.ir/\w+",msg)))
	joincORjoing = "joing" in msg or "joinc" in msg

	if joincORjoing: return joincORjoing
	else:
		for link in links:
			try:
				Type = bot.getInfoByUsername(link)["data"]["chat"]["abs_object"]["type"]
				if Type == "Channel":
					return True
			except KeyError: return False
			
# static variable
answered, sleeped, retries = [], False, {}
while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		open("id.txt","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins :
						#ID = loads(c.decrypt(getUserInfo(msg.get("author_object_guid")).json().get("data_enc"))).get("data").get("user").get("username")
						#sendMessage(guid, f"#اخطار @{ID}", msg["message_id"])
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "off" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, "کاربر با موفقیت بن شد ❗", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, "این کاربر ادمین است ❎", message_id=msg.get("message_id"))
							
						except IndexError:
							bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
							bot.sendMessage(target, "کاربر به دلیل رعایت نکردن #قوانین بن شد ✅", message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("!send") :

						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))

						bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("روبرتو کجایی"):
						bot.sendMessage(target, "دستشویی بودم😐💔", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چه خبر" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "سلامتی رهبر 😂🥲", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("بده"):
						bot.sendMessage(target, "نمیده", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلام" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "سلام چطوری جون دل؟😍", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😂😂😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "جون تو فقط بخند😍❤️", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("دانلود گریه"):
						bot.sendMessage(target, "خطا در دانلود گریه⁉️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "00:00" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "شاخ با موفقیت شناسایی و ثبت شد✅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مامانت کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "زهرا عشق امیر", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "زرا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "با مامانم چیکار داری؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "زهرا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "با مامانم چیکار داری؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "گدرت؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بچه بیا پایین سرمون درد گرفت", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "دانلود گدرت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, " https://دانلود-گدرت-با-لینک-مستقیم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ربات عمته من روبرتو هستم", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("❤️"):
						bot.sendMessage(target, "عاشقشی؟😍❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "روبات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "روبات ن روبرتو بگو 🥲", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بات ن روبرتو بگو 🥲", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "دانلود سطح" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, " https://دانلود-سطح-با-لینک-مستقیم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بابات کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پدرت", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بی گدرت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بی‌گدرت با موفقیت شناسایی و ثبت شد✅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "اره" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آجر پاره", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "باشه" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آفرین بچه حرف گوش کن👏", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عمت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بیشرف با عمم چیکار داری🙄", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "فحش بده" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "من بچه خوبیم با ادبم😌🤞", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هعی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آه نکش فدات شم😔", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عجب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خر مش رجب", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "درخواست نائنگی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "تموم کردم😁😅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سفید" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "سفید مورد نظر شناسایی شد ✅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "برقراری عزیز؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بلی جون دل", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "ایدی پدرت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "@MR_MESHKY", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("دانلود نت"):
						bot.sendMessage(target, "https://دانلود-نت-با-لینک-مستقیم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کمر نمونده برات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "هعی😔", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "جق می‌زنی؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آره دابش روزی 6 بار🤣❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بیو ساز فری فایر" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "@TOOLS_FF", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عمه داری؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اره @Alinia_zeynoosh", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کی میاد گیم؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نت ندارم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایدی امیر" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "2692329572", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "شماره بده" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "0992بقیه شو بدو ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "لینک" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "https://rubika.ir/joing/BIDDEGBG0OTFXBBIPNDUQDNZINIEPZEQ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خدافز" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدافز  عشقم ❤", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "دیوث" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "عمت😐🗿", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "what's your name" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "my name is roberto", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "حق" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "عا بمولا", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "آموزش" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آموزش روبرتو 🤖 :\n\n⭐ !font name\n\nبه جای name اسم خودتونو بزنید به اینگلیسی\n\n⭐ !tran hi\n\nبه جای hi کلمه ای که میخواین معنی کن بگید \n\n⭐ قابلیت دانستنی ، جوک ، حدیث ، تاریخ ، ذکر ، پینگ ، فونت و ترجمه به سرور متصل هستند وقتی ک امیر نت ندار من نمیتونم اینارو بگم \n\nقابلیت ارسال پیام ناشناس هم هست ک بعضی اوقات غیر فعال \n!send id سلام\n\nId = ایدی طرف رو بزارید", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("کنده"):
						bot.sendMessage(target, "روبیکا کنده به من چه😔", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کصپدرت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اقای تو دار ک اقای اون داشته باشه؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "پدرت کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "@MR_MESHKY", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "حسین" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "با داداشم چیکا داری؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "🖕" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بزا پشتت واس رشتت", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بی ادب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ببخشید😔", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "وات" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "لامپ صد وات😐", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "بای" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خداحافظ", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("بیا پایین"):
						bot.sendMessage(target, "به امید روزی که همه بچ های ایران بیان پایین", message_id=msg.get("message_id"))

					elif msg.get("text") == "شب خوش" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خوب بخوابی😴❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خودتی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بیترادب", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "روبرتو" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "جونم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کی نوب؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ممد و سجاد", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "چرا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "زیرا", message_id=msg.get("message_id"))

					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "فدات ط خوبی چخبرا ؟ 😊", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "سلامتی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "همیشه سلامت باشی گلم♥️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "فعلا" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خدافز عشقم 😁❤", message_id=msg.get("message_id"))

					elif msg.get("text") == "😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نخند مسواک گرون", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "چته؟😐😐", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نخند مسواک گرون", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "بیا پی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بابام میگ با غریبه چت نکن", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "هعب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اری هعب", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "امیر" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بابام چیکار داری؟", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "رل پی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پی چک 😁😅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کیر" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اه بی تربیت", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "رلم میشی؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بیا پی عکس بده", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "نوب" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نوب مورد نظر ثبت شد ✅", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "رل میزنی؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "اره چرا ک ن 😂❤", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "کی کون میده؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "من میدم🙂😂", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "مشکی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "رئیسمه فداش بشم من", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "💔" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نشکن🙂🥀", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "😐💔" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نشکن🙂🥀", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "اصل بده" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ربات پشتیبانی گپ هستم اطلاعاتم : @support_GP", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "ممنون" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "خواهش میکنم گلم💋😌", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "😐😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "😂😐", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "😂😂" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نخند مسواک گرون", message_id=msg.get("message_id"))

					elif msg.get("text") == "سجاد کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پرو ترین پروها تو خونشون", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "حسین کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پی‌سی پلیر نوبی در مشهد", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "س" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "معلمت بهت یاد نداده مثل آدم سلام کنی؟🤨", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ممد کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "ممد یک فرد فشاری تو بازی ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "امیر کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "سازنده من ۱۵ سالشه گیلانی ولی قزوین زندگی مکن😂😁", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "جواامان کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نوب سگ ترین نوبا", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ناشناس" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "https://abzarek.ir/service-p/msg/242623", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "میگم" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بگو", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "نه" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نه و نکمه😑", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("بمولا"):
						bot.sendMessage(target, "آره بمولا", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایمان کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "گدرتمند ترین رفیق امیر", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "رضا کیه؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "یک خرجم نوب", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "صلام" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "معلمت بهت یاد نداده مثل آدم سلام کنی؟🤨", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "نوب سگ" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "نوب سگ شناسایی شد✅", message_id=msg.get("message_id"))
					
					elif msg["text"].startswith("نت ندارم"):
						bot.sendMessage(target, "شماره بده دو بزنم واست", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("نت نی"):
						bot.sendMessage(target, "شماره بده  دو بزنم واست", message_id=msg.get("message_id"))

					elif msg.get("text") == "گدرت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "آره گدرت✌️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عمه" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "امیر بیا اهدا کننده عمه داریم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "درخواست لاواط" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بیا پی لاواط کنیم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "جون" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "بفرما بادمجون 🍆🍆", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "پشمام" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "پشمات", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "دمت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "چاکرم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "شرمنده" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "دشمنت شرمنده😍❤️", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عمتو" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "مامانتو🙈", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "دهنت" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "منم جر خوردم از خنده🤣", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "ایدی حسین" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "2848004516", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چی بلدی؟" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "لیست گدرت‌های روبرتو 🤖 :\n\n⭐ گفتگو با اعضا\n\n⭐ باز و قفل کردن گروه\n\nدستورات گدرت ها :\n\n⭐ !ping : گرفتن پینگ\n\n⭐ !tran : ترجمه اینگلیسی\n\n⭐ !font : ارسال فونت اینگلیسی\n\n⭐ !user : اطلاعات کاربر با ایدی\n\n⭐ !add : اد زدن کاربر با ایدی\n\n⭐ !send : ارسال پیام ناشناس\n\n⭐ بیوگرافی : دریافت بیوگرافی \n\n⭐ جوک بگو ، ذکر ، دانستنی ، حدیث ، پیشنهاد رمز ، ساعت ، تاریخ", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "چنل" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "@support_GP", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "عالی" and msg.get("author_object_guid") :
						
						bot.sendMessage(target, "چه خوب 😁❤", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("!add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "lock" :
						print(bot.setMembersAccess(target, []).text)
						bot.sendMessage(target, "گروه با موفقیت بسته شد 🔐", message_id=msg.get("message_id"))

					elif msg.get("text") == "unlock" :
						bot.setMembersAccess(target, ["SendMessages"])
						bot.sendMessage(target, "گروه با موفقیت باز شد 🔓", message_id=msg.get("message_id"))
						
					elif msg["text"].startswith("!font"):
						response = get(f"https://api.codebazan.ir/font/?text={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n\n".join(list(response["result"].values())[:55])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "متأسفانه نتیجه‌ای در بر نداشت ☹️", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("!tran"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "ترجمه به پی‌وی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "✖ خطا ✖", message_id=msg["message_id"])
					
					if  msg.get("text").startswith('!user @'):

						try:

							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'نام کاربر:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nبیوگرافی کاربر:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))

					elif msg.get("text").startswith("دانستنی"):
						try :
							response = get("http://api.codebazan.ir/danestani").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("حدیث"):
						try :
							response = get("http://api.codebazan.ir/hadis").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("بیوگرافی"):
						try :
							response = get("https://api.codebazan.ir/bio").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])		
							
					elif msg.get("text").startswith("!ping"):
						try :
							response = get("http://api.codebazan.ir/ping/?url=rubika.ir").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ذکر"):
						try :
							response = get("http://api.codebazan.ir/zekr").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])	
							
					elif msg["text"]=="پنل" and not msg["author_object_guid"] in admins: bot.sendMessage(target, "you are not an admin", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("تاریخ"):
						try :
							response = get("http://api.codebazan.ir/time-date/?td=date").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("جوک بگو"):
						try :
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("ساعت"):
						try :
							response = get("http://api.codebazan.ir/time-date/?td=timeen").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
							
					elif msg.get("text").startswith("پیشنهاد رمز"):
						try :
							response = get("https://api.codebazan.ir/password/?length=100").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
							
				else:
					if msg.get("text") == "on" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"هعب کار بدی کرد بن شد 😂", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گپ {name} خوش آمدید ⭐\n لطفا #قوانین را رعایت کنید ❤", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"️میموندی جناپ برنج خیس کردم 🥲", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گپ {name} خوش آمدید ⭐\n لطفا #قوانین را رعایت کنید ❤", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue