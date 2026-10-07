#!/usr/bin/env python3
import base64
"""Revotel static site generator. Usage: gen.py <outdir> <prod|preview>"""
import sys, os, json, html, shutil

OUT, MODE = sys.argv[1], sys.argv[2]
PREVIEW = MODE == "preview"
BASE = "https://www.revotel.in"
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
import datetime
TODAY = datetime.date.today().isoformat()

PHONE1, PHONE1_TEL, PHONE1_WA = "+91 81719 99631", "+918171999631", "918171999631"
EMAIL2 = "ravneet@revotel.in"
TAWK = """<!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/59562344e9c6d324a47381cd/default';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
</script>
<!--End of Tawk.to Script-->"""
FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800"
         "&family=Hanken+Grotesk:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap")

e = html.escape

# ---------- content ----------
SERVICES = [
 dict(slug="revenue-management", name="Hotel revenue management",
  short="Daily rate, inventory and channel decisions for your property, run by a revenue manager who reads your market.",
  title="Hotel Revenue Management Services in India | Revotel",
  desc="Outsourced hotel revenue management for independent hotels and resorts in Goa, Uttarakhand, Himachal, Madhya Pradesh, Dubai and Thailand. Rate strategy, forecasting and monthly performance reports.",
  h1="Hotel revenue management for independent properties",
  intro="Most independent hotels price by habit: last year's rate, a nervous discount, a copy of the hotel across the road. We take over the daily decisions on rate, inventory, restrictions and channel mix, and report back every month in numbers you can check against your own books.",
  does=["Daily rate and availability decisions across your room types and rate plans",
        "Competitor set tracking, so every price is set against what guests can actually book instead",
        "Demand forecasting by month, weekend, festival and local event",
        "Segment and channel mix review: OTA, direct, corporate, groups, travel agents",
        "Length-of-stay and minimum-stay rules for peak dates",
        "A monthly performance report covering occupancy, ADR, RevPAR, pick-up and channel cost"],
  who="Owners and general managers of hotels, resorts and boutique stays that have no full-time revenue manager, or that have one and still miss their targets.",
  faqs=[("What is hotel revenue management?","It is the practice of selling the right room to the right guest at the right time, at the right price, through the right channel. In daily work it means setting rates and restrictions from demand data, then checking the result against occupancy, ADR and RevPAR."),
        ("Do we need to change our channel manager or PMS?","Usually not. We work with the systems you already use. If your setup is holding you back, we say so in the first review and suggest what to change."),
        ("How do you charge?","We scope after a property review. Fees are either a monthly retainer or linked to the revenue improvement, depending on the property and what you prefer. Ask for a quote on the contact page.")]),
 dict(slug="hotel-launch", name="Hotel planning, development and launch",
  short="For owners building or opening a hotel: planning, positioning, pricing, distribution, content and the first 90 days.",
  title="New Hotel Launch & Pre-Opening Consultant in India | Revotel",
  desc="Hotel pre-opening consulting for owners building a new hotel. Market positioning, pricing, OTA setup, content and photography, and a launch plan for the first 90 days. Goa, Uttarakhand, Himachal, MP, Dubai, Thailand.",
  h1="Launch a new hotel with bookings already waiting",
  intro="A hotel that opens with weak listings, no reviews and guessed prices spends its first year catching up. We work with owners from the stage when the building is still being finished, so that on opening day the rooms are priced, listed, photographed and ready to sell.",
  does=["Market and competitor study for your location and segment",
        "Positioning: who the hotel is for, what it charges and why",
        "Opening rate strategy and rate plans for the first season",
        "OTA onboarding and channel manager setup, with listings built for search rank",
        "Content, room descriptions and a photo and video shoot plan",
        "Sales and review plan for the first 90 days after opening"],
  who="Owners, developers and families planning a new hotel, resort or villa property, and operators taking over an existing hotel under a new name.",
  faqs=[("How early should we start before opening?","Ideally three to four months before the opening date. That is enough time to build listings, shoot content and get the first bookings in ahead of launch. Earlier is better if you are still deciding on room mix or pricing."),
        ("Can you advise before the hotel is built?","Yes. Feasibility, room mix and the pricing you can realistically hold are easier to fix on paper than after construction. Contact us with your location and plan."),
        ("Do you stay on after the launch?","Most owners continue with revenue management after the opening period. It is optional; the launch plan is written so your own team can run it.")]),
 dict(slug="ota-distribution", name="OTA, distribution and marketing",
  short="Listings, rank, rate parity, promotions, commission cost and digital marketing across Booking.com, Agoda, MakeMyTrip and more.",
  title="OTA Management & Hotel Distribution Strategy | Revotel",
  desc="OTA management for hotels: Booking.com, Agoda, MakeMyTrip, Goibibo and Expedia. Better listings, higher search rank, rate parity, promotions and lower commission cost.",
  h1="OTA and distribution management for hotels",
  intro="OTAs bring most independent hotels a large share of their bookings, and take a large share of the revenue as commission. The aim is to get found, convert the search, and keep direct and low-cost channels growing alongside.",
  does=["Listing audit on each OTA: photos, descriptions, room mapping, policies",
        "Search rank work: content score, availability, rate competitiveness, review score",
        "Rate parity checks across channels and your own website",
        "Choosing which OTA promotions and programmes to join, and which to skip",
        "Extranet management and regular reviews with OTA account contacts",
        "Digital marketing and social media support to grow direct bookings",
        "Commission and channel cost reporting, so you see what each channel really costs"],
  who="Hotels that depend on OTAs, are slipping in search rank, or are paying commission on bookings they would have received anyway.",
  faqs=[("Which OTAs do you manage?","Booking.com, Agoda, MakeMyTrip, Goibibo, Expedia and the other channels connected to your property. We also review corporate, travel agent and direct channels."),
        ("Can you improve our ranking on Booking.com or MakeMyTrip?","Rank depends on content quality, price, availability, conversion and reviews. We work on each of these and measure the change in views, conversion and bookings. No one can guarantee a rank."),
        ("Will you cut our OTA commission?","We reduce what you pay by choosing programmes carefully and building direct and repeat business. Commission rates themselves are set by each OTA's agreement with you.")]),
 dict(slug="content-photography", name="Content writing and photoshoots",
  short="Room and property photography, video, and listing copy written to convert on OTAs, Google and your website.",
  title="Hotel Photoshoot & Content Writing Services in India | Revotel",
  desc="Hotel photography, video and content writing for OTA listings, Google and hotel websites. Room, property and amenity shoots and listing copy that helps hotels get found and booked.",
  h1="Hotel photoshoots and content writing",
  intro="Guests choose a hotel from its photos and its first lines of description, usually on a phone. Weak images and generic copy cost bookings on every channel. We shoot the property and write the content together, so what guests see matches what they find.",
  does=["Room, property and amenity photography planned shot by shot before the shoot",
        "Short video clips for OTAs, social media and the website",
        "Room and property descriptions written for search and for conversion",
        "Content for OTA listings, Google Business Profile and the hotel website",
        "Social media content for the property",
        "Content refresh after renovations, rebrands or a change in target guests"],
  who="New hotels preparing to open, existing hotels with dated photos, and properties whose listings do not match what guests actually get.",
  faqs=[("Do you travel for photoshoots?","Yes. We shoot on site at your property, in Goa and in the other destinations we cover. Travel is planned with you when we scope the shoot."),
        ("Can you write the content and shoot together?","Yes, and it works better that way. The shot list and the descriptions are planned from the same positioning."),
        ("Will you upload the content to our OTAs?","Yes. As part of our OTA and distribution work, we update your listings so the new content is live on each channel.")]),
 dict(slug="reputation-management", name="Reputation and review management",
  short="Review scores, responses and content across Google, TripAdvisor and the OTAs, which decide whether guests book.",
  title="Hotel Reputation & Review Management Services | Revotel",
  desc="Hotel online reputation management: review responses, score improvement and guest feedback loops across Google, TripAdvisor, Booking.com and MakeMyTrip.",
  h1="Hotel reputation and review management",
  intro="Guests read reviews before they compare prices. A half-point difference in score changes both conversion and the rate you can hold. We run the review process for you: collect, respond, learn and fix.",
  does=["Weekly review monitoring across Google, TripAdvisor and each OTA",
        "Professional responses written in your hotel's voice",
        "Guest feedback loop that catches problems before the guest leaves a review",
        "Review request process that brings in more happy guests' feedback",
        "Monthly summary of what guests praise and complain about, with fixes for your team",
        "Content refresh when reviews show the listing promises the wrong thing"],
  who="Hotels with a review score below their competitors, a few recent bad reviews, or a good product that guests rarely write about.",
  faqs=[("Can you remove negative reviews?","Genuine reviews cannot be removed. We respond to them well, report ones that break platform rules, and improve the experience that caused them."),
        ("How long does it take to improve a score?","Scores move as new reviews arrive, so the pace depends on your guest volume. Hotels with steady occupancy usually see movement within a few months."),
        ("Do you write fake reviews?","No. That breaks platform rules and puts your listing at risk.")]),
 dict(slug="training", name="Staff training and sales development",
  short="Front office, reservations and sales teams trained to sell rooms, handle OTA extranets and deal with reviews.",
  title="Hotel Staff Training: Sales, Front Office & Reservations | Revotel",
  desc="On-site and online training for hotel teams: selling rooms, upselling, OTA extranet handling, review response and revenue basics for front office and sales staff.",
  h1="Training for hotel sales and front office teams",
  intro="Revenue strategy only works if the people at the desk and on the phone carry it out. We train your team on the things that change results: quoting rates, upselling, handling enquiries and using the systems properly.",
  does=["Selling skills for front office and reservations: enquiry handling, quoting, closing",
        "Upselling room categories, meal plans and packages",
        "OTA extranet handling: availability, rates, restrictions, reservations",
        "Review response and guest recovery",
        "Revenue basics for managers: ADR, occupancy, RevPAR, pick-up and forecasting",
        "Follow-up checks after the session to confirm the changes stuck"],
  who="Hotel teams in any city, run on site or online, for owners who want staff to take part in the revenue plan instead of working around it.",
  faqs=[("Do you train on site or online?","Both. On-site sessions work best for front office and sales teams. Online sessions suit managers and multi-property groups."),
        ("How long is a training programme?","From a single half-day session to a monthly programme over a quarter. We recommend the format after talking to you about your team."),
        ("Can training be combined with revenue management?","Yes, and it usually works better that way. Your team learns the logic behind the rates we set.")]),
]

DESTS = [
 dict(slug="goa", name="Goa", places="North Goa, South Goa, Panaji, Candolim, Baga, Anjuna, Palolem",
  title="Hotel Consultant & Revenue Management in Goa | Revotel",
  desc="Hotel revenue management and launch consulting in Goa. Seasonal pricing for beach resorts, boutique hotels and villas: Christmas and New Year peaks, shoulder months and monsoon.",
  h1="Hotel revenue management in Goa",
  intro="Goa sells on a few weeks of very high demand and a long stretch of softer months. Hotels that price by habit leave money on the table at the peak and discount too early in the shoulder. We set rate and inventory strategy for beach resorts, boutique hotels and villas across North and South Goa.",
  rows=[("October to December","Season opens and demand builds toward Christmas and New Year","Open rates early, protect peak dates, set minimum stays for the last week of December"),
        ("January to March","Steady leisure, wedding and long-weekend demand","Price weekends and holiday weekends separately, balance OTA and direct"),
        ("April to May","Heat, domestic family travel and fewer international guests","Move to family and drive-in segments, package rooms with meals"),
        ("June to September","Monsoon and the lowest demand of the year","Protect rate floors, target short stays and local guests, avoid deep OTA discounting")],
  pains=["Heavy dependence on OTAs and the commission that comes with it","Rates that do not separate peak weeks from ordinary weeks","New or rebranded properties with no OTA rank and few reviews","Competition from villas and rentals on the same OTAs"],
  faqs=[("Do you work with hotels in both North and South Goa?","Yes. The two markets have different guests, rates and seasons, so we price them separately."),
        ("When should a new Goa hotel start planning its launch?","Ideally three to four months before opening, and before the season starts. Goa's best weeks are booked early."),
        ("Do you work with villas and small boutique stays?","Yes. Small properties often gain the most, since one pricing decision affects a large share of their year.")]),
 dict(slug="uttarakhand", name="Uttarakhand", places="Rishikesh, Dehradun, Mussoorie, Nainital, Jim Corbett, Haridwar, Auli",
  title="Hotel Consultant & Revenue Management in Uttarakhand | Revotel",
  desc="Hotel revenue management and launch consulting in Uttarakhand: Rishikesh, Mussoorie, Nainital, Jim Corbett and Dehradun. Pricing for summer peaks, Char Dham season, monsoon and winter weekends.",
  h1="Hotel revenue management in Uttarakhand",
  intro="Uttarakhand demand moves with the calendar and the roads: summer escapes from Delhi NCR, the Char Dham yatra, weekend drive-in trips, monsoon disruption and winter snow. We help hotels in Rishikesh, Mussoorie, Nainital, Corbett and the rest of the state price for each of those patterns.",
  rows=[("March to June","Summer peak and the Char Dham yatra season","Hold rates through the peak, use length-of-stay rules, plan for last-minute demand"),
        ("July to September","Monsoon, with road and landslide disruption in the hills","Flexible cancellation terms, local and short-stay offers, protect staff costs"),
        ("October to November","Clear weather, festivals and weddings","Raise rates for festival weekends, build wedding and group business"),
        ("December to February","Winter weekends, snow-viewing and New Year","Price New Year early, target weekend drive-in guests from Delhi NCR")],
  pains=["Weekday occupancy that falls sharply after the weekend rush","Monsoon months with cancellations and little forward booking","Pilgrimage and leisure guests who book through different channels","Owners without a trained reservations team in the hills"],
  faqs=[("Do you work with hotels in Rishikesh, Mussoorie and Corbett?","Yes. Each has its own guests and season, so strategy is set town by town."),
        ("Can you help with weekday occupancy in the hills?","Yes. Corporate offsites, schools, retreats and long-stay packages are the usual routes, along with weekday rates built around them."),
        ("Do you help new hotels in Uttarakhand?","Yes. Many new properties here open in a rush before peak season. We plan the listing, pricing and content around that date.")]),
 dict(slug="himachal-pradesh", name="Himachal Pradesh", places="Shimla, Manali, Dharamshala, Kasauli, Kasol, Kullu",
  title="Hotel Consultant & Revenue Management in Himachal Pradesh | Revotel",
  desc="Hotel revenue management and launch consulting in Himachal Pradesh: Manali, Shimla, Dharamshala, Kasauli and Kullu. Pricing for summer, snow season and monsoon.",
  h1="Hotel revenue management in Himachal Pradesh",
  intro="Himachal has two strong peaks, summer and winter snow, and a monsoon gap between them. Most demand arrives by road from Delhi, Punjab and Chandigarh, often at short notice. We build rate strategy around those drive-in patterns for hotels in Manali, Shimla, Dharamshala, Kasauli and Kullu.",
  rows=[("March to June","Summer peak, with the heaviest demand in May and June","Raise rates for weekends and holidays, require minimum stays, watch competitor sell-out"),
        ("July to August","Monsoon and road disruption","Flexible offers, direct bookings, long-stay and workation guests"),
        ("September to November","Autumn shoulder, with festivals and weddings","Rebuild rate after the monsoon, target couples and group travel"),
        ("December to February","Snow season and New Year, the winter peak","Open New Year rates early, price by snow-access and weekend demand")],
  pains=["Over-discounting in the monsoon, which then drags down the next peak","Large swings between peak weekends and ordinary weekdays","Properties off the main road that rely on OTA visibility","Seasonal staff turnover that weakens sales and service"],
  faqs=[("Do you work in Manali, Shimla and Dharamshala?","Yes, and in smaller markets such as Kasauli, Kullu and Kasol. Each market has its own mix of guests."),
        ("How do you price for snowfall and road closures?","We watch forecasts and competitor availability, and keep flexible rate plans ready, so that rates move with real conditions."),
        ("Can you help a hotel recover after a bad season?","Yes. We start with a review of rate, channel mix and reviews, and set a plan for the next season.")]),
 dict(slug="madhya-pradesh", name="Madhya Pradesh", places="Indore, Bhopal, Ujjain, Khajuraho, Pachmarhi, Kanha, Bandhavgarh, Omkareshwar",
  title="Hotel Consultant & Revenue Management in Madhya Pradesh | Revotel",
  desc="Hotel revenue management and launch consulting in Madhya Pradesh: Ujjain, Indore, Bhopal, Khajuraho, Pachmarhi and tiger reserve lodges. Pilgrimage, business and wildlife demand.",
  h1="Hotel revenue management in Madhya Pradesh",
  intro="Madhya Pradesh has three demand engines: pilgrimage in Ujjain and Omkareshwar, business travel in Indore and Bhopal, and wildlife tourism around Kanha and Bandhavgarh. Each needs a different pricing approach. We work with hotels in all three, and with owners preparing for the next Simhastha in Ujjain, expected in 2028.",
  rows=[("All year","Business travel in Indore and Bhopal, and steady pilgrimage in Ujjain","Corporate rates, weekday and weekend rate plans, group and festival pricing"),
        ("October to June","Wildlife season for tiger reserve lodges, since core zones are generally closed during the monsoon","Price by safari availability, book ahead in winter, package stays with safaris"),
        ("Festivals and religious dates","Sharp short peaks around major festivals and darshan days in Ujjain","Set rates early, use minimum stays and tight inventory control"),
        ("Monsoon","Quieter for leisure","Local, corporate and event business, with content refreshed for the next season")],
  pains=["Rates that treat pilgrimage dates like ordinary weekends","New hotels in Ujjain and Indore with strong buildings but weak OTA presence","Wildlife lodges with seasonal cash flow and uneven booking pace","Few revenue managers who know the state's smaller markets"],
  faqs=[("Do you work with hotels in Ujjain?","Yes. Ujjain demand moves with festivals, darshan crowds and long weekends, and requires tight inventory control on peak dates."),
        ("Can you help a hotel prepare for Simhastha 2028?","Yes. Hotels planning new rooms or a rebrand should start well in advance, since positioning, content and pricing take time to build."),
        ("Do you work with wildlife lodges near Kanha and Bandhavgarh?","Yes. Safari booking windows, season dates and international and domestic mix all affect pricing there.")]),
 dict(slug="dubai", name="Dubai", places="Dubai, Deira, Downtown, Marina, Jumeirah, Bur Dubai",
  title="Hotel Consultant & Revenue Management in Dubai | Revotel",
  desc="Hotel revenue management and OTA strategy for Dubai hotels and serviced apartments, with a focus on Indian outbound travellers, winter peak and summer low season.",
  h1="Hotel revenue management in Dubai",
  intro="Dubai is a highly competitive hotel market with a strong winter peak, a quiet summer and a stream of events that move rates sharply. Indian travellers are a large source market. We help Dubai hotels and serviced apartments set rates against a tight competitor set and reach guests in India.",
  rows=[("November to March","Winter peak with the highest rates of the year","Hold rates, manage minimum stays around holidays and big events"),
        ("April to May","Shoulder period, with Eid and school holiday dates moving each year","Plan around holiday calendars, adjust offers for families"),
        ("June to September","Summer low season","Package offers, longer-stay and staycation rates, source-market campaigns"),
        ("Event dates","Trade shows, festivals and sporting events cause sharp spikes","Track the event calendar, set rates and restrictions early")],
  pains=["A dense competitor set where small rate differences decide the booking","Heavy OTA commission and visibility competition","Weak reach into the Indian market","Summer occupancy that drops faster than the cost base"],
  faqs=[("Do you work with hotels in Dubai?","Yes. We work with hotels and serviced apartments, and with owners from India who invest in Dubai property."),
        ("Can you help us reach Indian travellers?","Yes. We review how your listings appear on OTAs that Indian guests use, and set offers and content for that market."),
        ("Do you manage rates remotely?","Yes. Revenue management does not need our team on site. We work through your channel manager and OTA extranets.")]),
 dict(slug="thailand", name="Thailand", places="Bangkok, Phuket, Pattaya, Krabi, Koh Samui, Chiang Mai",
  title="Hotel Consultant & Revenue Management in Thailand | Revotel",
  desc="Hotel revenue management and OTA strategy for hotels and resorts in Thailand: Bangkok, Phuket, Pattaya, Krabi and Chiang Mai. High season, green season and Indian traveller demand.",
  h1="Hotel revenue management in Thailand",
  intro="Thailand has a clear high season, a long green season, and festival spikes such as Songkran. Indian travellers are a large and growing segment for Bangkok, Phuket and Pattaya. We work with hotels and resorts in Thailand on rates, OTA positioning and reaching guests from India.",
  rows=[("November to February","High season, with peak rates around Christmas and New Year","Hold rates, require minimum stays for holiday weeks, manage OTA allocation"),
        ("March to April","Hot months, with Songkran in mid-April","Price festival dates separately, offer pool and family packages"),
        ("May to October","Green season and lower rates","Offer longer-stay and package rates, target regional and Indian travellers"),
        ("Year round","Bangkok city demand from business and transit travel","Weekday corporate rates, airport and city-event pricing")],
  pains=["Over-reliance on a single OTA","Discounting in the green season to levels that hurt the next high season","Listings that do not speak to Indian guests' needs, such as meals and family rooms","Owners who live in India and need remote revenue support"],
  faqs=[("Do you work with hotels in Phuket, Bangkok and Pattaya?","Yes. We work with hotels and resorts across Thailand, and also with Indian owners who run properties there."),
        ("Can you help attract Indian guests?","Yes. We review meal plans, room types, content and the OTAs used by Indian travellers, and set offers for that segment."),
        ("Is the work done remotely?","Yes. Rates and channel work run through your systems, with regular calls to review results.")]),
]

ALL_DEST_NAMES = [d["name"] for d in DESTS]
OTAS = ["MakeMyTrip", "Goibibo", "Booking.com", "Agoda", "Expedia", "Yatra", "Cleartrip", "Trip.com", "Airbnb", "Tripadvisor"]
OTA_LOGOS = [("gommt", "Go-MMT Group: MakeMyTrip, Goibibo, redBus", "#ffffff"), ("booking", "Booking.com", "#ffffff"), ("agoda", "Agoda", "#ffffff"),
  ("expedia", "Expedia", "#ffc50c"), ("yatra", "Yatra", "#ffffff"), ("cleartrip", "Cleartrip", "#ffffff"), ("tripcom", "Trip.com", "#ffffff"),
  ("airbnb", "Airbnb", "#ffffff"), ("tripadvisor", "Tripadvisor", "#33e0a1")]
def _ota_src(n):
    if PREVIEW:
        return "data:image/png;base64," + base64.b64encode(open(os.path.join(HERE, "ota", n + ".png"), "rb").read()).decode()
    return "/images/ota/" + n + ".png"

LAUNCH_STEPS = [
 ("Market and feasibility", "Competitor set, demand drivers, achievable rates and the realistic occupancy for your location and room mix."),
 ("Positioning and pricing", "Who the hotel is for, how it is described, and the opening rate plans for the first season."),
 ("Distribution setup", "Channel manager, OTA listings, rate parity and the channels you want to grow first."),
 ("Content and photography", "Room descriptions, photo and video plan, website copy and Google listing."),
 ("Launch and first 90 days", "Opening promotions, review plan, weekly rate and pick-up review, and a report at day 30, 60 and 90."),
]

HOME_FAQS = [
 ("What is hotel revenue management?","It is the practice of selling the right room to the right guest at the right time, at the right price, through the right channel. Revotel runs it for independent hotels and resorts: daily rates and inventory, channel mix, forecasting and a monthly report."),
 ("What is Foodle+?","Foodle+ is Revotel's hotel PMS, guest experience management system (GEMS) and POS, built with AI and powered by automation. Guests scan a QR code to make requests, which are routed to the PMS, or to WhatsApp if your hotel is connected through Meta. It syncs with STAAH and Aiosell."),
 ("Which channel managers do you work with?","STAAH and Aiosell. Foodle+ is compatible with both, and our revenue team can manage rates and inventory through either."),
 ("Who do you work with?","Independent hotels, resorts, boutique stays, villas and serviced apartments, and owners who are still building. We work in Goa, Uttarakhand, Himachal Pradesh, Madhya Pradesh, Dubai and Thailand, and take on other markets by discussion."),
 ("Can I use revenue management and Foodle+ separately?","Yes. Each works on its own. Used together, the revenue team works from your own PMS data."),
 ("How do I start?","Send a message on WhatsApp or the contact page with your property name, location and what you need. We reply with questions and a proposal after a short call."),
]

# ===== tech data + helpers (inserted before helpers) =====
TECH = [
 dict(slug="foodle-plus", name="Foodle+ (FP)", short="Our AI hotel PMS, guest experience system (GEMS) and POS, built with AI and powered by automation.",
  title="Foodle+ | AI Hotel PMS & Guest Experience System (GEMS) | Revotel",
  desc="Foodle+ is a hotel PMS, guest experience management system (GEMS) and POS built with AI and powered by automation. Syncs with STAAH and Aiosell. Guests scan a QR code in five languages.",
  h1="Foodle+: AI hotel PMS, guest experience system and POS",
  intro="Foodle+ (FP) is a hotel PMS, guest experience management system (GEMS) and POS, built with AI and powered by automation. It syncs with the STAAH and Aiosell channel managers. Use the PMS, the GEMS, or both, depending on what your hotel needs.",
  faqs=[("What is Foodle+?","Foodle+ is a hotel PMS and guest experience management system (GEMS), built by Revotel. Guests use a QR code to make requests, and AI and automation route those requests to the PMS or to WhatsApp."),
        ("Do I need WhatsApp to use the guest QR system?","No. Requests go directly to the PMS. If your hotel connects WhatsApp through Meta, requests can also be delivered on WhatsApp."),
        ("Does Foodle+ work with my channel manager?","Foodle+ syncs with STAAH and Aiosell. If you use another channel manager, ask us and we will check."),
        ("Can I use only the guest experience part?","Yes. The GEMS can run as a standalone product. You can also use the PMS alone, or the PMS integrated with your STAAH or Aiosell channel manager."),
        ("Which languages does the guest QR system support?","Five languages, including Hindi and English. Ask us for the full list."),
        ("How is Foodle+ priced?","Send us your room count and what you need and we will send a quote. Book a demo on WhatsApp to see the product first.")]),
 dict(slug="hotel-pms", name="Hotel PMS", short="Property management system with AI doing the analysis and backend work.",
  title="AI Hotel PMS Software in India | Foodle+ Property Management System",
  desc="Foodle+ is a hotel property management system (PMS) with AI handling analysis and backend work. Compatible with STAAH and Aiosell channel managers. Built for independent hotels and resorts.",
  h1="Hotel PMS software with AI behind it",
  intro="A property management system is what your front office runs on: reservations, rooms and guests in one place. The Foodle+ PMS adds AI that does the analysis and backend work, so your team spends less time on reports and more time with guests.",
  faqs=[("What is a hotel PMS?","A property management system is the software a hotel uses to manage reservations, rooms, guests and front-desk work in one place."),
        ("What does the AI do in the Foodle+ PMS?","The AI handles analysis and backend work for the PMS, so managers get the picture without building reports by hand."),
        ("Can the PMS connect to my channel manager?","Foodle+ is compatible with STAAH and Aiosell channel managers."),
        ("Is it suitable for a small independent hotel?","Foodle+ is built for independent hotels and resorts. Send your room count and we will recommend what you need.")]),
 dict(slug="guest-experience-system", name="Guest experience system (GEMS)", short="QR-based guest requests routed by automation and AI to the PMS or WhatsApp.",
  title="Hotel Guest Experience Management System (GEMS) with QR & WhatsApp | Revotel",
  desc="A QR-based guest experience management system for hotels. Guests scan, AI and automation route requests straight to your PMS or to WhatsApp via Meta integration.",
  h1="Guest experience management system (GEMS) for hotels",
  intro="Guests scan a QR code in the room or at the property and send a request. Automation and AI understand it and send it straight to the PMS, or to WhatsApp if your hotel is connected through Meta. No calls to the front desk, and nothing gets lost.",
  faqs=[("How does a guest use the GEMS?","The guest scans a QR code with their phone and uses it to order services, send housekeeping requests, order in-room dining, ask for a room upgrade or leave a review. The service is offered in five languages."),
        ("Where do the requests go?","Requests go to the Foodle+ PMS. If your hotel has WhatsApp connected through Meta, they are also delivered on WhatsApp."),
        ("What role does AI play?","Automation and AI read the request and send it to the right place, so staff receive clear tasks instead of phone calls."),
        ("Can GEMS be used without the Foodle+ PMS?","Yes. The GEMS is available as a standalone product, or together with the Foodle+ PMS.")]),
 dict(slug="channel-manager", name="Channel manager integration", short="STAAH and Aiosell channel managers, set up and managed with your revenue plan.",
  title="Hotel Channel Manager Setup: STAAH & Aiosell | Revotel",
  desc="Channel manager setup and management for hotels using STAAH or Aiosell. Foodle+ PMS is compatible with both. Rate parity, room mapping and OTA connectivity run by a revenue team.",
  h1="Channel manager setup for hotels: STAAH and Aiosell",
  intro="We do not build our own channel manager. We work with two established ones, STAAH and Aiosell, and the Foodle+ PMS is compatible with both. Because our revenue team sets the rates, your channel manager is configured around how you actually sell.",
  faqs=[("Which channel managers do you work with?","STAAH and Aiosell. Foodle+ is compatible with both."),
        ("Do you sell the channel manager?","We set up and manage your account on the channel manager that suits your hotel. Subscription terms come from the channel manager provider."),
        ("Can you take over my existing channel manager account?","If you already use STAAH or Aiosell, we can manage rates, inventory and OTA connections for you as part of revenue management."),
        ("Do I need Foodle+ to use your channel manager service?","No. Revenue management and channel manager work can be done with or without Foodle+.")]),
]
CHANNEL_MANAGERS = ["STAAH", "Aiosell"]
FOODLE = "https://foodleplus.com"

def spath(s):
    return s["slug"] if s["slug"] == "revenue-management" else "services/" + s["slug"]

def tpath(t):
    return "technology/" + t["slug"]


# ---------- helpers ----------
def depth_of(path):  # "" -> 0 ; "services/training" -> 2
    return len([p for p in path.split("/") if p])

def href(cur, target):
    """cur/target are page paths like '' or 'services/training'."""
    if not PREVIEW:
        return "/" if target == "" else "/" + target + "/"
    up = "../" * depth_of(cur)
    return up + ("index.html" if target == "" else target + "/index.html")

_LOGO_B64 = base64.b64encode(open(os.path.join(HERE, "logo.png"), "rb").read()).decode()
def logo_img():
    src = ("data:image/png;base64," + _LOGO_B64) if PREVIEW else "/images/logo.png"
    return f'<img src="{src}" alt="Revotel" width="136" height="34">'

def logo_svg():
    return ('<svg viewBox="0 0 28 28" aria-hidden="true"><rect x="2" y="15" width="5" height="11" rx="1" fill="#00c4cc"/>'
            '<rect x="9" y="9" width="5" height="17" rx="1" fill="#00c4cc"/><rect x="16" y="3" width="5" height="23" rx="1" fill="#e39b12"/>'
            '<rect x="23" y="11" width="3" height="15" rx="1" fill="#00c4cc" opacity=".55"/></svg>')

def faq_block(faqs):
    items = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faqs)
    return f'<div class="faq">{items}</div>'

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def crumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + ("/" if p == "" else "/" + p + "/")} for i, (n, p) in enumerate(items)]}

ORG = {
    "@context": "https://schema.org", "@type": "ProfessionalService", "@id": BASE + "/#org",
    "name": "Revotel", "url": BASE + "/",
    "description": "Hotel revenue management and hotel technology company. Builds the Foodle+ AI PMS and guest experience system; also provides hotel consulting, planning and development, OTA distribution, content and photoshoots.",
    "email": EMAIL2, "telephone": PHONE1_TEL,
    "areaServed": [{"@type": "AdministrativeArea", "name": "Goa"}, {"@type": "AdministrativeArea", "name": "Uttarakhand"},
                   {"@type": "AdministrativeArea", "name": "Himachal Pradesh"}, {"@type": "AdministrativeArea", "name": "Madhya Pradesh"},
                   {"@type": "City", "name": "Dubai"}, {"@type": "Country", "name": "Thailand"}],
    "serviceType": ["Hotel revenue management", "Hotel PMS software", "Guest experience management system", "Channel manager setup", "Hotel consulting", "Hotel planning and development", "OTA management", "Hotel photography and content writing", "Hotel reputation management", "Hotel staff training"],
    "sameAs": ["https://www.facebook.com/revotel.in/", "https://www.linkedin.com/in/revotel"],
}

def nav_html(cur):
    def a(t, p, key):
        cur_attr = ' aria-current="page"' if (cur == p or (p and cur.startswith(p + "/"))) else ""
        return f'<a href="{href(cur, p)}"{cur_attr}>{t}</a>'
    return ('<nav class="nav" aria-label="Main">' + a("Revenue management", "revenue-management", "r") + a("Technology", "technology", "t") + a("Results", "results", "x") + a("Insights", "insights", "i")
            + a("Services", "services", "s") + a("Destinations", "destinations", "d") + a("Contact", "contact", "c")
            + f'<a class="btn primary" href="https://wa.me/{PHONE1_WA}">WhatsApp us</a></nav>')

def footer_html(cur):
    svc = "".join(f'<li><a href="{href(cur, spath(s))}">{e(s["name"])}</a></li>' for s in SERVICES)
    tch = "".join(f'<li><a href="{href(cur, tpath(t))}">{e(t["name"])}</a></li>' for t in TECH)
    dst = "".join(f'<li><a href="{href(cur, "destinations/" + d["slug"])}">{e(d["name"])}</a></li>' for d in DESTS)
    return f'''<footer class="site-footer"><div class="foot-cols">
<div class="stack" style="gap:.6rem"><a class="brand" href="{href(cur, "")}">{logo_img()}</a>
<p class="muted" style="font-size:.95rem">Hotel revenue management and hotel technology, with consulting, content and launch support.</p>
<p class="copyline">{PHONE1}<br>{EMAIL2}</p></div>
<div><h3>Services</h3><ul>{svc}</ul></div>
<div><h3>Technology</h3><ul>{tch}</ul></div>
<div><h3>Destinations</h3><ul>{dst}</ul></div>
<div><h3>Company</h3><ul><li><a href="{href(cur, "results")}">Results</a></li><li><a href="{href(cur, "insights")}">Insights</a></li><li><a href="{href(cur, "about")}">About</a></li><li><a href="{href(cur, "contact")}">Contact</a></li>
<li><a href="https://www.linkedin.com/in/revotel">LinkedIn</a></li><li><a href="https://www.facebook.com/revotel.in/">Facebook</a></li><li><a href="{href(cur, "privacy")}">Privacy</a></li></ul></div></div>
<p class="fine">&copy; 2026 Revotel. Hotel consulting in India, Dubai and Thailand. Serving Goa, Pune, Bangalore, Kolkata, Rajasthan, Uttarakhand, Himachal Pradesh, Madhya Pradesh and Thailand.</p></footer>'''

def page(path, title, desc, body, schemas, og_type="website", noindex=False):
    canon = BASE + ("/" if path == "" else "/" + path + "/")
    css = f"<style>{CSS}</style>" if PREVIEW else f'<link rel="stylesheet" href="/css/style.css">'
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Revotel">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#00c4cc">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
{css}
{ld}
</head>
<body>
<header class="site-header"><a class="brand" href="{href(path, "")}">{logo_img()}</a>{nav_html(path)}</header>
<main class="wrap">
{body}
</main>
{footer_html(path)}
{TAWK}
</body>
</html>
'''

def crumbs_html(path, items):
    parts = []
    for i, (n, p) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f"<span>{e(n)}</span>")
        else:
            parts.append(f'<a href="{href(path, p)}">{e(n)}</a><span aria-hidden="true">/</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'

def cta_block(path, heading="Tell us about your property"):
    return f'''<aside class="cta"><div class="stack"><h2>{e(heading)}</h2>
<p>Send the property name, location and what you need. You get a reply from Ravneet, with questions and a proposal after a short call.</p></div>
<div class="stack"><div class="btn-row"><a class="btn primary" href="https://wa.me/{PHONE1_WA}">WhatsApp</a><a class="btn" href="{href(path, "contact")}">Contact form</a></div>
<div class="contact-lines"><span>{PHONE1}</span><span>{EMAIL2}</span></div></div></aside>'''

def pace_calendar():
    wk = ["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]
    data = [("6,200", 3, 62), ("7,400", 4, 90), ("5,100", 2, 48), ("4,300", 1, 28), ("4,200", 1, 24), ("4,400", 1, 30), ("4,900", 2, 44),
            ("5,600", 3, 58), ("8,200", 4, 96), ("6,800", 3, 70), ("4,500", 1, 32), ("4,300", 1, 26), ("4,600", 2, 38), ("5,200", 2, 50)]
    cells = ""
    for i, (rate, lvl, pick) in enumerate(data):
        cells += (f'<div class="cell l{lvl}"><b>{wk[i % 7]}</b><span class="bar"><u style="height:{max(8, pick * 26 // 100)}px"></u></span>'
                  f'<i>{rate}</i></div>')
    return f'''<div class="pace" role="img" aria-label="Illustrative fourteen-night calendar showing room rate in rupees and rooms already booked, with weekends highest">
<div class="pace-head"><strong>Next 14 nights</strong><span>rate in &#8377; &middot; bar = rooms booked</span></div>
<div class="pace-grid">{cells}</div>
<p class="pace-note">Illustrative view of what a revenue manager reads every day. Sample numbers, not client data.</p></div>'''

PAGES = []  # (path, html)

def add(path, title, desc, body, schemas, **kw):
    PAGES.append((path, page(path, title, desc, body, schemas, **kw)))

# ---------- home ----------
def flow_html():
    return '''<ol class="flow" aria-label="How a guest request travels through Foodle+">
<li><h3>Guest scans the QR code</h3><p>In the room or around the property, on their own phone.</p></li>
<li><h3>Automation and AI read the request</h3><p>The request is understood and sorted.</p></li>
<li><h3>It reaches your team</h3><p>Straight to the PMS, or to WhatsApp if connected through Meta.</p></li></ol>'''

def build_home():
    p = ""
    rm = [s_ for s_ in SERVICES if s_["slug"] == "revenue-management"][0]
    others = [s_ for s_ in SERVICES if s_["slug"] != "revenue-management"]
    dest_rows = "".join(
        f'<div class="row"><div><h3><a href="{href(p, "destinations/" + d["slug"])}">{e(d["name"])}</a></h3></div>'
        f'<div><p>{e(d["places"])}</p></div></div>' for d in DESTS)
    svc_rows = "".join(
        f'<div class="row"><div><h3><a href="{href(p, spath(s))}">{e(s["name"])}</a></h3></div>'
        f'<div><p>{e(s["short"])}</p></div></div>' for s in others)
    tech_rows = "".join(
        f'<li><a href="{href(p, tpath(t))}">{e(t["name"])}</a></li>' for t in TECH[1:])
    steps = "".join(f"<li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d in LAUNCH_STEPS)
    chips = "".join(f"<li>{e(o)}</li>" for o in OTAS)
    _li = lambda hid: "".join(f'<li{" aria-hidden=true" if hid else ""} style="background:{bg}"><img src="{_ota_src(n)}" alt="{"" if hid else e(nm)}" height="56" loading="lazy"></li>' for n, nm, bg in OTA_LOGOS)
    ota_strip = ('<section class="ota" aria-label="OTA partners"><div class="ota-head"><h2>Our OTA partners</h2>'
        '<p class="muted">Your rooms, live on the channels guests actually book from. We manage rates and inventory across all of them.</p></div>'
        '<ul class="ota-track">' + _li(False) + _li(True) + '</ul></section>')
    cms = "".join(f"<li>{e(o)}</li>" for o in CHANNEL_MANAGERS)
    _items = [(o["title"], o["desc"], "insights/" + o["slug"]) for o in POSTS[:3]]
    _items += [(a_["h1"], a_["intro"], "insights/" + a_["slug"]) for a_ in ARTICLES][:max(0, 3 - len(_items))]
    ins_rows = "".join(f'<div class="row"><div><h3><a href="{href(p, u_)}">{e(t_)}</a></h3></div><div><p>{e(d_)}</p></div></div>' for t_, d_, u_ in _items)
    rm_does = "".join(f"<li>{e(x)}</li>" for x in rm["does"][:5])
    body = f'''
<section class="hero"><div class="stack">
<h1>Sell every room at the right rate, on the right channel.</h1>
<p class="lead">Revotel runs hotel revenue management for independent hotels and resorts, and builds the technology behind it: Foodle+, our AI hotel PMS and guest experience system. Based in Goa, working across Goa, Uttarakhand, Himachal, Madhya Pradesh, Dubai and Thailand.</p>
<div class="btn-row"><a class="btn primary" href="https://wa.me/{PHONE1_WA}">Talk to Ravneet on WhatsApp</a><a class="btn" href="{href(p, "revenue-management")}">How revenue management works</a></div>
</div>{pace_calendar()}</section>
{ota_strip}

<section class="section"><div class="split"><div class="stack"><h2>Revenue management</h2><p class="muted">{e(rm["short"])}</p>
<a class="btn" href="{href(p, "revenue-management")}">Revenue management services</a></div>
<ul class="checks">{rm_does}</ul></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Results</h2><p class="muted">Same months, compared with before and last year. Hotel names withheld.</p><a class="btn" href="{href(p, "results")}">See the results</a></div>
<div class="rows"><div class="row"><div><h3>80-room beach resort</h3></div><div><p><span class="pct up">{sgn(RES["B"]["rev"])}</span> revenue and <span class="pct up">{sgn(RES["B"]["rn"])}</span> room nights, July to September 2026.</p></div></div>
<div class="row"><div><h3>33-room hotel, North Goa</h3></div><div><p><span class="pct up">{sgn(_g(sum(RES["A3"]["rv26"][:8]),sum(RES["A3"]["rv24"][:8])))}</span> revenue and <span class="pct up">{sgn(_g(sum(RES["A3"]["rn26"][:8]),sum(RES["A3"]["rn24"][:8])))}</span> room nights, January to August 2026 against the same months in 2024, before we started.</p></div></div></div></div></section>

<section class="section tech"><div class="stack" style="gap:1.6rem"><div class="stack"><h2>Technology: Foodle+</h2>
<p class="lead">Foodle+ is our hotel PMS, guest experience management system (GEMS) and POS, built with AI and powered by automation. It syncs with STAAH and Aiosell. Use the PMS, the GEMS, or both. Guests scan a QR code to order services, housekeeping, in-room dining, room upgrades and leave reviews, in five languages.</p></div>
{flow_html()}
<div class="btn-row"><a class="btn primary" href="{href(p, tpath(TECH[0]))}">See Foodle+</a><a class="btn" href="{FOODLE}" rel="noopener">Visit foodleplus.com</a><a class="btn" href="https://wa.me/{PHONE1_WA}?text=I%20would%20like%20a%20Foodle%2B%20demo">Book a demo on WhatsApp</a></div>
<ul class="chips alt">{tech_rows}</ul></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Reports you can check</h2><p class="muted">Every month you receive a performance report, compared with your competitor set and your own targets.</p></div>
<div class="stack"><div class="table-scroll"><table><thead><tr><th>Measure</th><th>What it tells you</th><th>Where you see it</th></tr></thead><tbody>
<tr><td>Occupancy</td><td>How many available rooms were sold</td><td>Monthly report</td></tr>
<tr><td>ADR</td><td>Average rate achieved per room sold</td><td>Monthly report</td></tr>
<tr><td>RevPAR</td><td>Revenue per available room, occupancy and rate together</td><td>Monthly report</td></tr>
<tr><td>Pick-up</td><td>How fast future dates are filling, compared with last year</td><td>Weekly update</td></tr>
<tr><td>Channel cost</td><td>Commission paid by channel and what it returned</td><td>Monthly report</td></tr>
<tr><td>Review score</td><td>Score and trend on Google, TripAdvisor and each OTA</td><td>Monthly report</td></tr></tbody></table></div>
<p class="caption">Measures included in every Revotel report. Targets are agreed with you at the start.</p></div></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Where we work</h2><p class="muted">Each market has its own seasons, guests and competitors. Pricing that works in Goa fails in the hills.</p></div>
<div class="rows">{dest_rows}</div></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Also from Revotel</h2><p class="muted">Consulting, content and training that sit around revenue management and technology.</p></div>
<div class="rows">{svc_rows}</div></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Planning a new hotel?</h2><p class="muted">The best time to talk to us is before the building is finished. This is how a launch usually runs.</p>
<a class="btn" href="{href(p, "services/hotel-launch")}">Hotel planning and development</a></div>
<ol class="steps">{steps}</ol></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Channels and systems</h2><p class="muted">We work through your own accounts and your channel manager, so you keep control of your data.</p></div>
<div class="stack"><div class="stack" style="gap:.5rem"><h3>Channel managers</h3><ul class="chips">{cms}</ul></div>
<div class="stack" style="gap:.5rem"><h3>Sales channels</h3><ul class="chips">{chips}</ul></div></div></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Insights</h2><p class="muted">Guides for hotel owners.</p><a class="btn" href="{href(p, "insights")}">All insights</a></div>
<div class="rows">{ins_rows}</div></div></section>

<section class="section"><div class="split"><div class="stack"><h2>Common questions</h2></div>{faq_block(HOME_FAQS)}</div></section>
{cta_block(p, "Want more from every room?")}
'''
    add("", "Hotel Revenue Management & AI Hotel PMS in India | Revotel",
        "Revotel: hotel revenue management for independent hotels and resorts, plus Foodle+, our AI hotel PMS and guest experience system. Goa, Uttarakhand, Himachal, Madhya Pradesh, Dubai, Thailand.",
        body, [ORG, faq_schema(HOME_FAQS)])

def tech_page(t):
    p = tpath(t)
    crumbs = [("Home", ""), ("Technology", "technology"), (t["name"], p)]
    cm = "".join(f"<li>{e(x)}</li>" for x in CHANNEL_MANAGERS)
    others = "".join(f'<li><a href="{href(p, tpath(o))}">{e(o["name"])}</a></li>' for o in TECH if o["slug"] != t["slug"])
    extra = ""
    if t["slug"] == "foodle-plus":
        extra = f'''<section class="section"><div class="split"><div class="stack"><h2>Three ways to use Foodle+</h2><p class="muted">Take what your hotel needs. Each option works on its own.</p></div><div class="rows">
<div class="row"><div><h3>PMS on its own</h3></div><div><p>The <a href="{href(p, tpath(TECH[1]))}">property management system</a> for reservations, rooms, guests and front-desk work, with AI doing the analysis and backend work.</p></div></div>
<div class="row"><div><h3>PMS with your channel manager</h3></div><div><p>The PMS integrated with <a href="{href(p, tpath(TECH[3]))}">STAAH or Aiosell</a>, so rates, inventory and bookings stay in sync.</p></div></div>
<div class="row"><div><h3>GEMS as a standalone product</h3></div><div><p>The <a href="{href(p, tpath(TECH[2]))}">guest experience management system</a>, used by itself. Guests scan a QR code on their phone and the requests reach your team.</p></div></div></div></div></section>
<section class="section"><div class="split"><div class="stack"><h2>What guests can do with the QR code</h2><p class="muted">No app to install. Available in five languages, including Hindi and English.</p></div>
<ul class="checks"><li>Order hotel services</li><li>Send housekeeping requests</li><li>Order food with in-room dining</li><li>Ask for a room upgrade</li><li>Leave a review</li><li>Become a lead your team can follow up, with lead generation management built in</li></ul></div></section>
<section class="section"><div class="split"><div class="stack"><h2>More about Foodle+</h2></div><div class="stack"><p>Foodle+ also has its own website with features, use cases and demo booking.</p><div class="btn-row"><a class="btn primary" href="{FOODLE}" rel="noopener">Visit foodleplus.com</a></div></div></div></section>'''
    if t["slug"] in ("foodle-plus", "guest-experience-system"):
        extra += f'''<section class="section"><div class="split"><div class="stack"><h2>How a guest request travels</h2></div>{flow_html()}</div></section>'''
    if t["slug"] in ("hotel-pms",):
        extra += '''<section class="section"><div class="split"><div class="stack"><h2>What the AI does</h2></div><p>The AI handles analysis and backend work for the PMS. Managers see what is happening at the property without building reports by hand, and the revenue team can work from the same data.</p></div></section>'''
    if t["slug"] == "channel-manager":
        extra += f'''<section class="section"><div class="split"><div class="stack"><h2>Channel managers we use</h2></div><div class="stack"><ul class="chips">{cm}</ul><p class="muted">Both are established channel managers. We set up and manage your account, and our revenue team sets the rates through it.</p></div></div></section>'''
    else:
        extra += f'''<section class="section"><div class="split"><div class="stack"><h2>Works with your channel manager</h2></div><div class="stack"><ul class="chips">{cm}</ul><p class="muted">Foodle+ syncs with STAAH and Aiosell. <a href="{href(p, tpath(TECH[3]))}">Read about channel manager setup</a>.</p></div></div></section>'''
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>{e(t["h1"])}</h1><p class="lead">{e(t["intro"])}</p>
<div class="btn-row"><a class="btn primary" href="https://wa.me/{PHONE1_WA}?text=I%20would%20like%20a%20Foodle%2B%20demo">Book a demo on WhatsApp</a><a class="btn" href="{FOODLE}" rel="noopener">Visit foodleplus.com</a></div></div></section>
{extra}
<section class="section"><div class="split"><div class="stack"><h2>Questions</h2></div>{faq_block(t["faqs"])}</div></section>
<section class="section"><div class="split"><div class="stack"><h2>More technology</h2></div><ul class="checks">{others}<li><a href="{href(p, "revenue-management")}">Revenue management</a></li></ul></div></section>
{cta_block(p, "See Foodle+ at your hotel")}'''
    schemas = [ORG, crumb_schema(crumbs), faq_schema(t["faqs"])]
    if t["slug"] == "foodle-plus":
        schemas.append({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "Foodle+", "alternateName": "FP",
                        "applicationCategory": "BusinessApplication", "applicationSubCategory": "Hotel property management system",
                        "description": t["desc"], "publisher": {"@id": BASE + "/#org"}, "url": BASE + "/" + p + "/"})
    add(p, t["title"], t["desc"], body, schemas)

def hub_tech():
    p = "technology"
    crumbs = [("Home", ""), ("Technology", "technology")]
    rows = "".join(
        f'<div class="row"><div><h3><a href="{href(p, tpath(t))}">{e(t["name"])}</a></h3></div>'
        f'<div><p>{e(t["short"])}</p><a class="more" href="{href(p, tpath(t))}">Read more</a></div></div>' for t in TECH)
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>Hotel technology from Revotel</h1>
<p class="lead">Foodle+ is our AI hotel PMS, guest experience system and POS. We pair it with channel managers we trust and a revenue team that sets the rates.</p></div></section>
<section class="section"><div class="rows">{rows}</div></section>{cta_block(p, "See Foodle+ at your hotel")}'''
    add(p, "Hotel Technology: AI PMS, Guest Experience & Channel Manager | Revotel",
        "Hotel technology from Revotel: Foodle+ AI PMS, QR-based guest experience management system, and channel manager setup with STAAH and Aiosell.",
        body, [ORG, crumb_schema(crumbs)])

def hub_services():
    p = "services"
    rows = "".join(
        f'<div class="row"><div><h3><a href="{href(p, spath(s))}">{e(s["name"])}</a></h3></div>'
        f'<div><p>{e(s["short"])}</p><a class="more" href="{href(p, spath(s))}">Read more</a></div></div>' for s in SERVICES)
    crumbs = [("Home", ""), ("Services", "services")]
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>Hotel services</h1>
<p class="lead">Revenue management and technology lead what we do. These services support them, from the first plan for a new hotel to the photos on your listings.</p></div></section>
<section class="section"><div class="rows">{rows}</div>
</section>{cta_block(p)}'''
    add(p, "Hotel Consulting, Content & Distribution Services | Revotel",
        "Hotel services from Revotel: revenue management, planning and development, OTA and marketing, content and photoshoots, reputation management and staff training.",
        body, [ORG, crumb_schema(crumbs)])

def hub_dests():
    p = "destinations"
    rows = "".join(
        f'<div class="row"><div><h3><a href="{href(p, "destinations/" + d["slug"])}">{e(d["name"])}</a></h3></div>'
        f'<div><p>{e(d["places"])}</p><a class="more" href="{href(p, "destinations/" + d["slug"])}">Hotel consulting in {e(d["name"])}</a></div></div>' for d in DESTS)
    crumbs = [("Home", ""), ("Destinations", "destinations")]
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>Destinations we work in</h1>
<p class="lead">We work on hotels across India's leisure, pilgrimage and business markets, and in Dubai and Thailand. Other markets by discussion.</p></div></section>
<section class="section"><div class="rows">{rows}</div></section>{cta_block(p)}'''
    add(p, "Hotel Consultant Across India, Dubai & Thailand | Revotel",
        "Hotel consulting and revenue management in Goa, Uttarakhand, Himachal Pradesh, Madhya Pradesh, Dubai and Thailand.",
        body, [ORG, crumb_schema(crumbs)])

def service_page(s):
    p = spath(s)
    crumbs = [("Home", ""), (s["name"], p)] if s["slug"] == "revenue-management" else [("Home", ""), ("Services", "services"), (s["name"], p)]
    does = "".join(f"<li>{e(x)}</li>" for x in s["does"])
    dl = "".join(f'<li><a href="{href(p, "destinations/" + d["slug"])}">{e(d["name"])}</a></li>' for d in DESTS)
    others = "".join(f'<li><a href="{href(p, spath(o))}">{e(o["name"])}</a></li>' for o in SERVICES if o["slug"] != s["slug"]) + f'<li><a href="{href(p, tpath(TECH[0]))}">Foodle+ AI hotel PMS</a></li>'
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>{e(s["h1"])}</h1><p class="lead">{e(s["intro"])}</p>
<div class="btn-row"><a class="btn primary" href="https://wa.me/{PHONE1_WA}">Ask about this service</a><a class="btn" href="{href(p, "contact")}">Contact form</a></div></div></section>
<section class="section"><div class="split"><div class="stack"><h2>What is included</h2></div><ul class="checks">{does}</ul></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Who it is for</h2></div><p>{e(s["who"])}</p></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Markets</h2><p class="muted">Available in all the destinations we cover.</p></div><ul class="chips">{dl}</ul></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Questions</h2></div>{faq_block(s["faqs"])}</div></section>
<section class="section"><div class="split"><div class="stack"><h2>Related services</h2></div><ul class="checks">{others}</ul></div></section>
{cta_block(p)}'''
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["desc"],
                  "provider": {"@id": BASE + "/#org"}, "serviceType": s["name"], "url": BASE + "/" + p + "/",
                  "areaServed": ALL_DEST_NAMES}
    add(p, s["title"], s["desc"], body, [ORG, svc_schema, crumb_schema(crumbs), faq_schema(s["faqs"])])

def dest_page(d):
    p = "destinations/" + d["slug"]
    crumbs = [("Home", ""), ("Destinations", "destinations"), (d["name"], p)]
    rows = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in d["rows"])
    pains = "".join(f"<li>{e(x)}</li>" for x in d["pains"])
    svc = "".join(f'<li><a href="{href(p, spath(s))}">{e(s["name"])}</a></li>' for s in SERVICES)
    others = "".join(f'<li><a href="{href(p, "destinations/" + o["slug"])}">{e(o["name"])}</a></li>' for o in DESTS if o["slug"] != d["slug"])
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>{e(d["h1"])}</h1><p class="lead">{e(d["intro"])}</p>
<p class="muted">Markets covered: {e(d["places"])}</p>
<div class="btn-row"><a class="btn primary" href="https://wa.me/{PHONE1_WA}">Discuss your {e(d["name"])} property</a><a class="btn" href="{href(p, "contact")}">Contact form</a></div></div></section>
<section class="section"><div class="split"><div class="stack"><h2>How demand moves in {e(d["name"])}</h2><p class="muted">General patterns. Exact dates change each year, so we plan from the live calendar.</p></div>
<div class="table-scroll"><table><thead><tr><th>Period</th><th>Demand pattern</th><th>What we do</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Where hotels struggle here</h2></div><ul class="checks">{pains}</ul></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Services for {e(d["name"])} hotels</h2></div><ul class="checks">{svc}<li><a href="{href(p, tpath(TECH[0]))}">Foodle+ AI hotel PMS and guest experience system</a></li></ul></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Questions</h2></div>{faq_block(d["faqs"])}</div></section>
<section class="section"><div class="split"><div class="stack"><h2>Other destinations</h2></div><ul class="chips">{others}</ul></div></section>
{cta_block(p, "Hotel in " + d["name"] + "? Let's talk.")}'''
    add(p, d["title"], d["desc"], body, [ORG, crumb_schema(crumbs), faq_schema(d["faqs"])])

def about_page():
    p = "about"
    crumbs = [("Home", ""), ("About", "about")]
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>A hotel consultant who works next to the owner</h1>
<p class="lead">Revotel is led by Ravneet. We work closely with owners and general managers, because the best results come from knowing the property, the market and the people running it.</p></div></section>
<section class="section"><div class="split"><div class="stack"><h2>How we work</h2></div><ul class="checks">
<li>One point of contact who knows your property, not a rotating account team</li>
<li>Decisions backed by data from your market and your competitor set</li>
<li>Plain monthly reports you can read in ten minutes and check against your own books</li>
<li>Work done through your systems, so you keep control of your accounts and data</li>
<li>Honest advice, including when the answer is to change a room mix, a channel manager or a price you are attached to</li></ul></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Where we are based</h2></div><p>Our team works from Goa, Pune, Bangalore and Kolkata, and with properties in Rajasthan, Uttarakhand, Himachal Pradesh, Madhya Pradesh, Dubai and Thailand.</p></div></section>
{cta_block(p)}'''
    add(p, "About Revotel | Hotel Consultants in India", "Revotel is a hotel consulting firm led by Ravneet, working with owners and general managers on hotel launches, revenue management and distribution.",
        body, [ORG, crumb_schema(crumbs)])

def contact_page():
    p = "contact"
    crumbs = [("Home", ""), ("Contact", "contact")]
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>Contact Revotel</h1>
<p class="lead">Tell us about your property. The quickest reply comes on WhatsApp.</p></div></section>
<section class="section"><div class="split"><div class="stack"><h2>Reach us directly</h2>
<p class="copyline">{PHONE1}</p><p class="copyline">{EMAIL2}</p>
<div class="btn-row"><a class="btn primary" href="https://wa.me/{PHONE1_WA}">Open WhatsApp</a></div></div>
<form id="enquiry" novalidate>
<div class="two"><label for="f-name">Your name<input id="f-name" name="name" autocomplete="name"></label>
<label for="f-phone">Phone or WhatsApp<input id="f-phone" name="phone" autocomplete="tel"></label></div>
<div class="two"><label for="f-prop">Property name<input id="f-prop" name="property"></label>
<label for="f-loc">Location<input id="f-loc" name="location" placeholder="For example, Candolim, Goa"></label></div>
<label for="f-need">What do you need?<select id="f-need" name="need">
<option>New hotel launch</option><option>Revenue management</option><option>OTA and distribution</option><option>Reputation and reviews</option><option>Staff training</option><option>Not sure yet</option></select></label>
<label for="f-msg">Message<textarea id="f-msg" name="message"></textarea></label>
<div class="btn-row"><button class="btn primary" type="submit" id="send-wa">Send on WhatsApp</button><button class="btn" type="button" id="send-mail">Send by email</button></div>
<p class="caption" id="form-note">This opens WhatsApp or your email app with your message filled in. Nothing is stored on this site.</p></form></div></section>'''
    script = f'''<script>
(function(){{
  var f=document.getElementById("enquiry"); if(!f) return;
  function text(){{
    var v=function(id){{return (document.getElementById(id).value||"").trim();}};
    return "Hello Revotel,\\nName: "+v("f-name")+"\\nPhone: "+v("f-phone")+"\\nProperty: "+v("f-prop")+"\\nLocation: "+v("f-loc")+"\\nNeed: "+v("f-need")+"\\n"+v("f-msg");
  }}
  f.addEventListener("submit",function(ev){{ev.preventDefault();
    window.open("https://wa.me/{PHONE1_WA}?text="+encodeURIComponent(text()),"_blank","noopener");}});
  document.getElementById("send-mail").addEventListener("click",function(){{
    window.location.href="mailto:{EMAIL2}?subject="+encodeURIComponent("Enquiry from revotel.in")+"&body="+encodeURIComponent(text());}});
}})();
</script>'''
    html_ = page(p, "Contact Revotel | Hotel Consultants", "Contact Revotel for hotel launch, revenue management and OTA consulting. WhatsApp +91 81719 99631 or email ravneet@revotel.in.",
                 body + script, [ORG, crumb_schema(crumbs)])
    PAGES.append((p, html_))

def not_found():
    body = f'''<section class="hero single"><div class="stack"><h1>This page has moved</h1>
<p class="lead">Try the home page, our services or the contact page.</p>
<div class="btn-row"><a class="btn primary" href="{href("", "")}">Home</a><a class="btn" href="{href("", "services")}">Services</a><a class="btn" href="{href("", "contact")}">Contact</a></div></div></section>'''
    return page("404", "Page not found | Revotel", "Page not found.", body, [], noindex=True)


# ---------- results ----------
RES = json.load(open(os.path.join(HERE, "results.json")))
MONTHS = [("01", "January"), ("02", "February"), ("03", "March"), ("04", "April"), ("05", "May")]

def sgn(v, d=0):
    r = round(v, d)
    if r == 0: r = 0.0
    return ("+" if r > 0 else "−" if r < 0 else "") + f"{abs(r):.{d}f}%"

def pct_span(v):
    cls = "up" if round(v) >= 0 else "down"
    return f'<span class="pct {cls}">{sgn(v)}</span>'

def kpi_row(rn, adr, rev):
    items = [("Room nights", rn), ("ADR", adr), ("RevPAR*", rev), ("Revenue", rev)]
    return '<div class="kpis">' + "".join(
        f'<div class="kpi{" neg" if round(v) < 0 else ""}"><strong>{sgn(v)}</strong><span>{l}</span></div>' for l, v in items) + '</div>'

def index_chart(rn, adr, rev):
    mx = max(100 + rn, 100 + adr, 100 + rev)
    rows = ""
    for label, g in [("Room nights", rn), ("ADR", adr), ("RevPAR*", rev), ("Revenue", rev)]:
        rows += (f'<div class="index-row"><b>{label}</b><div class="index-bars">'
                 f'<div class="ibar"><i style="width:{100 / mx * 80:.1f}%"></i><span>last year 100</span></div>'
                 f'<div class="ibar now"><i style="width:{(100 + g) / mx * 80:.1f}%"></i><span>this year {100 + g:.0f}</span></div></div></div>')
    return f'<div class="index-chart" role="img" aria-label="Index chart: same period last year equals 100">{rows}</div>'

def _g(a, b):
    return 100 * (a / b - 1)

def results_page():
    p = "results"
    crumbs = [("Home", ""), ("Results", "results")]
    B = RES["B"]
    D = RES["A3"]
    sm = lambda x, i, j: sum(x[i:j])
    def trio(r1, v1, r0, v0):
        return (_g(r1, r0), _g(v1 / r1, v0 / r0), _g(v1, v0))
    k_before = trio(sm(D["rn26"], 0, 8), sm(D["rv26"], 0, 8), sm(D["rn24"], 0, 8), sm(D["rv24"], 0, 8))
    k_yoy = trio(sm(D["rn26"], 0, 9), sm(D["rv26"], 0, 9), sm(D["rn25"], 0, 9), sm(D["rv25"], 0, 9))
    NAMES = ["January", "February", "March", "April", "May", "June", "July", "August"]
    mrows = ""
    for i, name in enumerate(NAMES):
        mrows += (f'<tr><td>{name}</td><td class="num">{pct_span(_g(D["rn26"][i], D["rn24"][i]))}</td>'
                  f'<td class="num">{pct_span(_g(D["rv26"][i], D["rv24"][i]))}</td>'
                  f'<td class="num">{pct_span(_g(D["rv25"][i], D["rv24"][i]))}</td></tr>')
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>Results from hotels we work with</h1>
<p class="lead">Growth for the same months, from online booking data. Hotel names are withheld to protect our clients.</p></div></section>

<section class="section"><div class="stack" style="gap:1.6rem"><div class="stack" style="gap:.5rem"><h2>33-room 4-star hotel, North Goa</h2>
<div class="result-meta"><span>Before and after Revotel started, same months</span><span>Online bookings through the channel manager</span></div></div>
<div class="stack" style="gap:.6rem"><h3>January to August 2026 compared with January to August 2024, before we started</h3>
{kpi_row(*k_before)}</div>
<div class="stack" style="gap:.6rem"><h3>Latest year on year: January to September 2026 compared with January to September 2025</h3>
{kpi_row(*k_yoy)}</div>
<div class="split"><div class="stack"><h3>Month by month</h3><p class="muted">Each month against the same month in 2024. The last column shows 2025, the first full year with us.</p></div>
<div class="stack"><div class="table-scroll"><table><thead><tr><th>Month</th><th class="num">Room nights 2026</th><th class="num">Revenue 2026</th><th class="num">Revenue 2025</th></tr></thead><tbody>{mrows}</tbody></table></div>
<p class="caption">Counted by the month the booking was made. Online bookings only, not total hotel business. Room nights grew faster than revenue: the average rate per room night is lower than in 2024. *RevPAR is calculated on 33 rooms in all periods, so its growth matches revenue growth.</p></div></div></div></section>

<section class="section"><div class="stack" style="gap:1.6rem"><div class="stack" style="gap:.5rem"><h2>80-room 4-star luxury beach resort</h2>
<div class="result-meta"><span>July to September 2026 compared with July to September 2025</span><span>Online bookings through the channel manager</span></div></div>
{kpi_row(B["rn"], B["adr"], B["rev"])}
<div class="split"><div class="stack"><h3>Same period last year = 100</h3><p class="muted">Room nights and ADR each grew by about a third. Together they raised revenue by more than two thirds.</p></div>
<div class="stack">{index_chart(B["rn"], B["adr"], B["rev"])}
<p class="caption">Revenue is before tax. *RevPAR is calculated on 80 rooms in both periods, so its growth matches revenue growth.</p></div></div></div></section>

<section class="section"><div class="split"><div class="stack"><h2>How we measure</h2></div><ul class="checks">
<li>Room nights: nights sold, counting each room separately</li>
<li>ADR: average daily rate, revenue divided by room nights</li>
<li>RevPAR: revenue per available room, calculated on the hotel's room count</li>
<li>Revenue: room revenue before tax</li></ul></div></section>
{cta_block(p, "Want numbers like these for your hotel?")}'''
    add(p, "Hotel Revenue Management Results & Case Studies | Revotel",
        "Before-and-after and year-on-year results from hotels using Revotel revenue management: room nights, ADR, RevPAR and revenue growth. Hotel names withheld.",
        body, [ORG, crumb_schema(crumbs)])


# ---------- insights ----------
ARTICLES = [
 dict(slug="revpar-adr-occupancy-explained", date="2026-10-06",
  title="RevPAR, ADR and Occupancy Explained for Hotel Owners | Revotel",
  desc="What RevPAR, ADR and occupancy mean, how to calculate each, and which hotel owners should watch every week. With a worked example.",
  h1="RevPAR, ADR and occupancy: what hotel owners should track",
  intro="Three numbers describe most of a hotel's room performance. Knowing how they connect tells you whether to raise rates, sell more rooms, or both.",
  sections=[
   ("Occupancy", ["Occupancy is the share of your available rooms that were sold.", "FORMULA:Occupancy = rooms sold ÷ rooms available", "A high occupancy figure alone can hide a problem. A hotel that is always full may be priced too low."]),
   ("ADR", ["ADR is average daily rate: the average price you got for each room sold.", "FORMULA:ADR = room revenue ÷ rooms sold", "ADR rises when you sell better room types, get higher rates, or give fewer discounts."]),
   ("RevPAR", ["RevPAR is revenue per available room. It counts every room you have, sold or not, so it shows occupancy and rate together.", "FORMULA:RevPAR = room revenue ÷ rooms available = occupancy × ADR", "Example with made-up numbers: a 40-room hotel sells 24 rooms in a night at an average of ₹5,000. Occupancy is 60%, ADR is ₹5,000, room revenue is ₹1,20,000, and RevPAR is ₹3,000."]),
   ("Which one to watch", ["Track all three, but make RevPAR the headline. If occupancy rises and RevPAR falls, you are selling rooms too cheaply. If ADR rises and RevPAR falls, you are pricing out guests.", "Many owners also track GOPPAR, gross operating profit per available room, which brings costs into the picture.", "Compare each number with the same period last year and with your competitor set, not with last month. Hotels have strong seasons and last month is rarely a fair comparison."]),
  ]),
 dict(slug="revenue-management-for-small-hotels", date="2026-10-06",
  title="Revenue Management for Small Hotels: Where to Start | Revotel",
  desc="A practical starting point for independent and small hotels: competitor set, seasonal pricing, pick-up tracking, channel mix and rate rules.",
  h1="Revenue management for small hotels: where to start",
  intro="You do not need expensive software to begin. Most small hotels gain from a few disciplined habits, applied every week.",
  sections=[
   ("1. Choose a competitor set", ["List five to eight hotels that your guests actually compare you with: same area, similar quality, similar price. Check their rates for the same dates you are selling."]),
   ("2. Study last year by month and day of week", ["Look at occupancy and ADR for each month and for weekdays against weekends. This shows your real peaks and your real quiet periods, which are often different from what the team assumes."]),
   ("3. Set a rate floor and a rate range", ["Decide the lowest rate you will accept for each room type, and the range you will price within on peak, normal and quiet dates. A floor stops panic discounting."]),
   ("4. Watch pick-up", ["Pick-up is how many rooms you have booked for a future date compared with the same point last year. If a date is filling faster than usual, raise the rate. If it is slower, act early with offers aimed at the right segment."]),
   ("5. Review channel mix every week", ["Check how many bookings come from each OTA, from your website, from corporate and from agents, and what each costs after commission. Then decide where to push."]),
   ("6. Keep rates consistent", ["The same room should not have very different prices across channels. Review parity regularly."]),
   ("When to get help", ["If you do these steps and still miss targets, or if nobody on the team has time, an outside revenue manager can run the daily decisions and give you a monthly report."]),
  ]),
 dict(slug="new-hotel-ota-setup-timeline", date="2026-10-06",
  title="How Early Should a New Hotel Set Up OTA Listings? | Revotel",
  desc="A timeline for new hotel owners: when to finalise positioning, shoot photos, connect the channel manager and open OTA listings before launch.",
  h1="How early should a new hotel set up its OTA listings?",
  intro="Hotels that open with thin listings and no reviews spend their first months catching up. A simple timeline avoids that.",
  sections=[
   ("About four months before opening", ["Settle positioning: who the hotel is for, what it charges and why. Study nearby competitors and decide your opening rate plans."]),
   ("About three months before", ["Plan content and book the photo and video shoot for when rooms, lobby and common areas are finished. Write room and property descriptions."]),
   ("About two months before", ["Choose and set up the channel manager. Map rooms and rate plans, and connect your PMS if you have one. Prepare your Google Business Profile and website."]),
   ("About six weeks before", ["Submit OTA listings. Verification and approval times vary by OTA and can take days or weeks, so leave room for corrections."]),
   ("At opening", ["Open sales with controlled inventory and tested rates. Make sure staff know how to use each extranet and how to respond to reviews."]),
   ("First 90 days", ["Review rates and pick-up weekly. Ask every guest for feedback and a review, and answer every review. Early reviews shape your search rank for the months that follow."]),
   ("A note on dates", ["Every property is different. If your opening date is close, tell us and we will compress the plan."]),
  ]),
 dict(slug="how-to-choose-a-channel-manager", date="2026-10-06",
  title="How to Choose a Channel Manager for Your Hotel | Revotel",
  desc="What to check before choosing a hotel channel manager: OTA connections, PMS integration, speed, support, reporting, pricing and data ownership.",
  h1="How to choose a channel manager for your hotel",
  intro="A channel manager sends your rates and availability to every OTA at once and brings bookings back. A poor choice causes overbookings and lost time, so check these points first.",
  sections=[
   ("OTA connections you need", ["List the OTAs you sell on today and the ones you want to add. Confirm the channel manager has live, two-way connections to each."]),
   ("PMS integration", ["If you use a PMS, check that bookings flow into it automatically and that availability updates go back out. Manual re-entry causes errors."]),
   ("Speed and reliability", ["Ask how quickly a change reaches the OTAs and what happens when an OTA connection fails."]),
   ("Support", ["You will need help at awkward hours, especially in season. Ask about support hours, response times and who you actually speak to."]),
   ("Reports", ["You need booking, revenue and channel reports that you can read and export, so you can see what each channel really delivers."]),
   ("Pricing and contract", ["Compare subscription fees, setup fees, per-booking charges and the contract term. Ask what happens if you leave."]),
   ("Data ownership", ["Make sure you can export your bookings and rates history, and that the account is in your hotel's name."]),
   ("Our view", ["We work with STAAH and Aiosell, and the Foodle+ PMS is compatible with both. The right choice depends on your property, your OTAs and your team. Contact us and we will recommend one after a short call."]),
  ]),
 dict(slug="reduce-ota-commission", date="2026-10-06",
  title="How to Reduce OTA Commission Without Losing Bookings | Revotel",
  desc="Practical ways hotels can lower OTA commission cost: grow direct bookings, repeat guests and corporate business, join programmes carefully and track net revenue by channel.",
  h1="How to reduce OTA commission without losing bookings",
  intro="OTAs bring guests you might not reach alone, and charge commission for it. The goal is not to leave the OTAs. It is to depend on them less and spend wisely on them.",
  sections=[
   ("Know what each channel costs", ["Work out net revenue per channel: room revenue minus commission and any promotion cost. A booking that looks cheap can leave you with less than a direct booking at a higher rate."]),
   ("Grow direct bookings", ["Make your website easy to book on a phone, show real photos and clear prices, and offer a reason to book direct, such as a better room, a late checkout or a meal credit. Answer WhatsApp enquiries quickly."]),
   ("Win repeat guests", ["Collect contact details at check-in with permission, and message past guests before your peak season."]),
   ("Build corporate and group business", ["Local companies, wedding planners and travel agents book directly and often repeat."]),
   ("Join OTA programmes carefully", ["Programmes that increase visibility usually raise commission. Join them for dates when you need the extra demand, not by default."]),
   ("Avoid deep blanket discounts", ["Discounts on every date lower your ADR and teach guests to wait. Target them at quiet dates and specific segments."]),
   ("Review monthly", ["Check channel mix and cost every month and adjust. A revenue manager can do this for you and report the result."]),
  ]),
]

def prose_html(sections):
    out = ""
    for h, paras in sections:
        out += f"<h2>{e(h)}</h2>"
        for t in paras:
            out += f'<p class="formula">{e(t[8:])}</p>' if t.startswith("FORMULA:") else f"<p>{e(t)}</p>"
    return f'<div class="prose">{out}</div>'

def article_page(a):
    p = "insights/" + a["slug"]
    crumbs = [("Home", ""), ("Insights", "insights"), (a["h1"], p)]
    related = "".join(f'<li><a href="{href(p, "insights/" + o["slug"])}">{e(o["h1"])}</a></li>' for o in ARTICLES if o["slug"] != a["slug"])
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>{e(a["h1"])}</h1><p class="lead">{e(a["intro"])}</p>
<p class="article-meta">By Ravneet, Revotel &middot; {a["date"]}</p></div></section>
<section class="section">{prose_html(a["sections"])}</section>
<section class="section"><div class="split"><div class="stack"><h2>Related</h2></div><ul class="checks">{related}
<li><a href="{href(p, "revenue-management")}">Hotel revenue management services</a></li></ul></div></section>
{cta_block(p, "Talk to a hotel revenue consultant")}'''
    art = {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["desc"],
           "datePublished": a["date"], "dateModified": a["date"], "author": {"@type": "Person", "name": "Ravneet"},
           "publisher": {"@id": BASE + "/#org"}, "mainEntityOfPage": BASE + "/" + p + "/"}
    add(p, a["title"], a["desc"], body, [ORG, art, crumb_schema(crumbs)], og_type="article")

def hub_insights():
    p = "insights"
    crumbs = [("Home", ""), ("Insights", "insights")]
    prow = "".join(
        f'<div class="row"><div><h3><a href="{href(p, "insights/" + o["slug"])}">{e(o["title"])}</a></h3><p class="muted">{_pretty_date(o["date"])}</p></div>'
        f'<div><p>{e(o["desc"])}</p></div></div>' for o in POSTS)
    posts_sec = f'<section class="section"><div class="split"><div class="stack"><h2>Latest posts</h2><p class="muted">Short notes from Ravneet on hotel revenue, distribution and technology. Also on <a href="https://www.linkedin.com/in/revotel" rel="noopener">LinkedIn</a>.</p></div><div class="rows">{prow}</div></div></section>' if POSTS else ""
    rows = "".join(
        f'<div class="row"><div><h3><a href="{href(p, "insights/" + a["slug"])}">{e(a["h1"])}</a></h3></div>'
        f'<div><p>{e(a["intro"])}</p></div></div>' for a in ARTICLES)
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>Hotel revenue and technology insights</h1>
<p class="lead">Notes and plain-language guides for hotel owners on pricing, distribution, launches and technology.</p></div></section>
{posts_sec}
<section class="section"><div class="split"><div class="stack"><h2>Guides</h2></div><div class="rows">{rows}</div></div></section>{cta_block(p)}'''
    add(p, "Hotel Revenue Management Insights & Guides | Revotel",
        "Posts and guides for hotel owners: RevPAR and ADR, revenue management for small hotels, OTA setup timelines, channel managers and OTA commission.",
        body, [ORG, crumb_schema(crumbs)])

def privacy_page():
    p = "privacy"
    crumbs = [("Home", ""), ("Privacy", "privacy")]
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>Privacy</h1><p class="muted">Last updated 6 October 2026</p></div></section>
<section class="section"><div class="prose">
<h2>What this site collects</h2><p>This site does not store your details. The contact form creates a message on your own device and opens WhatsApp or your email app. Nothing you type is sent to our servers until you send the message yourself.</p>
<h2>Messages you send us</h2><p>When you contact us on WhatsApp, by email or by phone, we use your details only to reply and to provide the service you ask for. We do not sell them.</p>
<h2>Third parties</h2><p>Pages load fonts from Google Fonts, which means Google receives your browser's request. WhatsApp links open WhatsApp, which has its own privacy policy.</p>
<h2>Client data</h2><p>Results shown on this site come from client booking data, with hotel names and guest details removed.</p>
<h2>Contact</h2><p>Questions about this page: {EMAIL2}.</p></div></section>'''
    add(p, "Privacy | Revotel", "How Revotel handles information on this website.", body, [ORG, crumb_schema(crumbs)])

# ---------- LinkedIn posts (managed from /admin/, stored in posts.json) ----------
import re as _re, datetime as _dt

def _slugify(t):
    s = _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return s[:60].strip("-") or "post"

def _load_posts():
    fp = os.path.join(HERE, "posts.json")
    if not os.path.exists(fp):
        return []
    try:
        raw = json.load(open(fp, encoding="utf-8"))
    except Exception:
        return []
    out, used = [], set(a["slug"] for a in ARTICLES)
    for r in sorted(raw, key=lambda x: (x.get("date", ""), str(x.get("id", ""))), reverse=True):
        title, text, url = str(r.get("title", "")).strip(), str(r.get("text", "")).strip(), str(r.get("url", "")).strip()
        if not title or not text:
            continue
        slug = _slugify(title)
        if slug in used:
            slug = slug + "-" + str(r.get("id", ""))[-5:]
        used.add(slug)
        paras = [x.strip() for x in _re.split(r"\n\s*\n", text) if x.strip()]
        flat = " ".join(paras)
        desc = flat if len(flat) <= 155 else flat[:152].rsplit(" ", 1)[0] + "..."
        out.append(dict(id=r.get("id"), slug=slug, title=title, text=text, paras=paras, desc=desc, date=str(r.get("date", TODAY))[:10], url=url))
    return out

POSTS = _load_posts()

def _pretty_date(d):
    try:
        x = _dt.date.fromisoformat(d); return f"{x.day} {x:%B %Y}"
    except Exception:
        return d

def post_page(po):
    p = "insights/" + po["slug"]
    crumbs = [("Home", ""), ("Insights", "insights"), (po["title"], p)]
    paras = "".join("<p>" + e(x).replace("\n", "<br>") + "</p>" for x in po["paras"])
    li = f'<a class="btn" href="{e(po["url"])}" rel="noopener" target="_blank">See the original on LinkedIn</a>' if po["url"] else ""
    related = "".join(f'<li><a href="{href(p, "insights/" + o["slug"])}">{e(o["title"])}</a></li>' for o in POSTS[:5] if o["slug"] != po["slug"])
    rel_block = f'<section class="section"><div class="split"><div class="stack"><h2>More from Ravneet</h2></div><ul class="checks">{related}<li><a href="{href(p, "insights")}">All insights</a></li></ul></div></section>'
    body = f'''<section class="hero single"><div class="stack">{crumbs_html(p, crumbs)}<h1>{e(po["title"])}</h1>
<p class="article-meta">By Ravneet, Revotel &middot; {_pretty_date(po["date"])}</p></div></section>
<section class="section"><div class="prose">{paras}</div><div class="btn-row" style="margin-top:1.6rem">{li}<a class="btn primary" href="https://wa.me/{PHONE1_WA}">Talk to Ravneet on WhatsApp</a></div></section>
{rel_block}
{cta_block(p, "Talk to a hotel revenue consultant")}'''
    art = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": po["title"], "description": po["desc"],
           "datePublished": po["date"], "dateModified": po["date"], "author": {"@type": "Person", "name": "Ravneet", "sameAs": "https://www.linkedin.com/in/revotel"},
           "publisher": {"@id": BASE + "/#org"}, "mainEntityOfPage": BASE + "/" + p + "/"}
    if po["url"]:
        art["sameAs"] = po["url"]
    add(p, po["title"] + " | Revotel", po["desc"], body, [ORG, art, crumb_schema(crumbs)], og_type="article")

ADMIN_HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Revotel admin</title>
<style>
:root{--bg:#f2f6f6;--card:#fff;--ink:#0a2a31;--muted:#4b6870;--line:#d3e0e1;--accent:#00a9b0;--down:#c0304a}
@media (prefers-color-scheme: dark){:root{--bg:#071c21;--card:#0d2a31;--ink:#e6f2f3;--muted:#93b0b5;--line:#1e3f46;--accent:#00c4cc;--down:#ff8097}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;padding:20px}
.wrap{max-width:760px;margin:0 auto;display:grid;gap:16px}
h1{font-size:1.5rem;margin:6px 0}h2{font-size:1.1rem;margin:0 0 8px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;display:grid;gap:12px}
label{display:grid;gap:4px;font-weight:600;font-size:.92rem}label span{font-weight:400;color:var(--muted);font-size:.85rem}
input,textarea{font:inherit;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px;width:100%}
textarea{min-height:220px;resize:vertical}
button{font:inherit;font-weight:600;border:0;border-radius:999px;padding:10px 20px;background:var(--accent);color:#03262a;cursor:pointer}
button.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}button.del{background:transparent;color:var(--down);border:1px solid var(--down)}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;justify-content:space-between;border-top:1px solid var(--line);padding-top:10px}
.row a{color:var(--ink)}.msg{padding:10px 12px;border-radius:8px;background:var(--bg);border:1px solid var(--line)}.err{color:var(--down)}
.hide{display:none}small{color:var(--muted)}
</style></head><body><div class="wrap">
<h1>Revotel admin</h1>
<div id="login" class="card"><label>Password<input id="pw" type="password" autocomplete="current-password"></label><div><button id="go">Log in</button></div><div id="lmsg" class="err"></div></div>
<div id="app" class="hide">
<div class="card"><h2 id="ftitle">Add a LinkedIn post</h2>
<label>LinkedIn post link<span>Open the post on LinkedIn, click the three dots, Copy link to post.</span><input id="url" placeholder="https://www.linkedin.com/posts/..."></label>
<label>Headline<span>This becomes the page title on Google. Leave blank to use the first line of the post.</span><input id="title" maxlength="140"></label>
<label>Post text<span>Paste the full text of your post. Google can only read words that are on your site, so this is what brings search traffic. Leave a blank line between paragraphs.</span><textarea id="text"></textarea></label>
<label>Date<input id="date" type="date"></label>
<div style="display:flex;gap:8px;flex-wrap:wrap"><button id="save">Publish</button><button class="ghost hide" id="cancel">Cancel edit</button></div><div id="smsg" class="msg hide"></div></div>
<div class="card"><h2>Published posts</h2><div id="list"><small>Loading...</small></div></div>
<div><button class="ghost" id="out">Log out</button></div></div></div>
<script>
const $=id=>document.getElementById(id);let PW=sessionStorage.getItem("rv_pw")||"",POSTS=[],EDIT=null;
async function api(body){const r=await fetch("/.netlify/functions/admin",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(Object.assign({password:PW},body))});let j={};try{j=await r.json()}catch(e){}if(!r.ok)throw new Error(j.error||("Error "+r.status));return j}
function show(ok){$("login").classList.toggle("hide",ok);$("app").classList.toggle("hide",!ok)}
function today(){const d=new Date();return d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0")}
function msg(t,err){const m=$("smsg");m.textContent=t;m.className="msg"+(err?" err":"");}
function esc(s){return s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}
function render(){const l=$("list");if(!POSTS.length){l.innerHTML="<small>No posts yet.</small>";return}
l.innerHTML=POSTS.map(p=>`<div class="row"><div><b>${esc(p.title)}</b><br><small>${esc(p.date)}</small></div><div><button class="ghost" data-e="${p.id}">Edit</button> <button class="del" data-d="${p.id}">Delete</button></div></div>`).join("")}
async function load(){const j=await api({action:"list"});POSTS=j.posts;render()}
async function login(){PW=$("pw").value||PW;try{await load();sessionStorage.setItem("rv_pw",PW);show(true);$("date").value=today()}catch(e){$("lmsg").textContent=e.message;show(false)}}
function reset(){EDIT=null;["url","title","text"].forEach(i=>$(i).value="");$("date").value=today();$("ftitle").textContent="Add a LinkedIn post";$("cancel").classList.add("hide")}
$("go").onclick=login;$("pw").addEventListener("keydown",e=>{if(e.key==="Enter")login()});
$("out").onclick=()=>{sessionStorage.removeItem("rv_pw");PW="";show(false)};
$("cancel").onclick=reset;
$("save").onclick=async()=>{let title=$("title").value.trim(),text=$("text").value.trim();if(!title)title=text.split(/\n/)[0].slice(0,100);
try{$("save").disabled=true;msg("Saving...");const j=await api({action:EDIT?"edit":"add",id:EDIT,url:$("url").value.trim(),title,text,date:$("date").value});POSTS=j.posts;render();reset();msg("Saved. The website updates in about a minute.")}catch(e){msg(e.message,true)}finally{$("save").disabled=false}};
$("list").onclick=async e=>{const d=e.target.dataset.d,ed=e.target.dataset.e;
if(d&&confirm("Delete this post from the website?")){try{const j=await api({action:"delete",id:d});POSTS=j.posts;render();msg("Deleted. The website updates in about a minute.")}catch(x){msg(x.message,true)}}
if(ed){const p=POSTS.find(x=>String(x.id)===ed);EDIT=p.id;$("url").value=p.url||"";$("title").value=p.title;$("text").value=p.text;$("date").value=p.date;$("ftitle").textContent="Edit post";$("cancel").classList.remove("hide");scrollTo(0,0)}};
if(PW)login();
</script></body></html>'''

# ---------- build ----------
build_home(); hub_services(); hub_dests(); hub_tech()
for t in TECH: tech_page(t)
for s in SERVICES: service_page(s)
for d in DESTS: dest_page(d)
results_page(); hub_insights()
for a_ in ARTICLES: article_page(a_)
for po_ in POSTS: post_page(po_)
privacy_page(); about_page(); contact_page()

if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
for path, content in PAGES:
    d = os.path.join(OUT, path) if path else OUT
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(content)

if not PREVIEW:
    os.makedirs(os.path.join(OUT, "images"))
    shutil.copy(os.path.join(HERE, "logo.png"), os.path.join(OUT, "images", "logo.png"))
    shutil.copytree(os.path.join(HERE, "ota"), os.path.join(OUT, "images", "ota"))
    os.makedirs(os.path.join(OUT, "css"))
    open(os.path.join(OUT, "css", "style.css"), "w", encoding="utf-8").write(CSS)
    open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(not_found())
    urls = "".join(f"  <url><loc>{BASE}{'/' if p == '' else '/' + p + '/'}</loc><lastmod>{TODAY}</lastmod></url>\n" for p, _ in PAGES)
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(OUT, ".htaccess"), "w").write(
"""# Apache (GoDaddy cPanel hosting). Keeps old Simplotel URLs working so Google keeps their ranking.
RedirectMatch 301 ^/our-services/revenue-management\\.html$ /revenue-management/
RedirectMatch 301 ^/our-services/?.*$ /services/
RedirectMatch 301 ^/contact-us/contact-us\\.html$ /contact/
RedirectMatch 301 ^/plan-your-trip/.*$ /contact/
RedirectMatch 301 ^/sitemap\\.html$ /sitemap.xml
ErrorDocument 404 /404.html
""")
    open(os.path.join(OUT, "_redirects"), "w").write(
"""# Netlify / Cloudflare Pages redirects for old Simplotel URLs
/our-services/revenue-management.html /revenue-management/ 301
/our-services/* /services/ 301
/contact-us/contact-us.html /contact/ 301
/plan-your-trip/* /contact/ 301
/sitemap.html /sitemap.xml 301
""")
os.makedirs(os.path.join(OUT, "admin"), exist_ok=True)
open(os.path.join(OUT, "admin", "index.html"), "w", encoding="utf-8").write(ADMIN_HTML)
if not PREVIEW:
    open(os.path.join(OUT, "_headers"), "w").write("/admin/*\n  X-Robots-Tag: noindex, nofollow\n  Cache-Control: no-store\n")
print(len(PAGES), "pages ->", OUT)
