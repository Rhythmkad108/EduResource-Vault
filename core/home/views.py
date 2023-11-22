from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Course
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="/")
def homePage(request):
    return render(request, "index.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passw = request.POST.get("pass")
        user = authenticate(request, username=username, password=passw)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return HttpResponse("Username or Password is Wrong!")

    return render(request, "login.html")


def registerPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirmpassword")
        if pass1 != pass2:
            return HttpResponse("Both the passwords should match!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("/")

    return render(request, "register.html")


def logoutPage(request):
    logout(request)
    return redirect("/")


# Semester Pages
# Sem 1
def sem1Page(request):
    return render(request, "sem1.html")


def edPage(request):
    data = get_course_info("E Drawing")
    return render(request, "sem1/ed.html", {"info": data})


def ieeePage(request):
    data = get_course_info("IEEE")
    return render(request, "sem1/ieee.html", {"info": data})


def chemPage(request):
    data = get_course_info("Chemistry")
    return render(request, "sem1/chemistry.html", {"info": data})


def computingPage(request):
    data = get_course_info("Intro to Computing")
    return render(request, "sem1/computing.html", {"info": data})


def calculusPage(request):
    data = get_course_info("Calculus")
    return render(request, "sem1/calculus.html", {"info": data})


# Sem 2
def sem2Page(request):
    return render(request, "sem2.html")


def evs1Page(request):
    data = get_course_info("EVS 1")
    return render(request, "sem2/evs1.html", {"info": data})


def probPage(request):
    data = get_course_info("Probability")
    return render(request, "sem2/probability.html", {"info": data})


def evs2Page(request):
    data = get_course_info("EVS 2")
    return render(request, "sem2/evs2.html", {"info": data})


def physicsPage(request):
    data = get_course_info("Physics")
    return render(request, "sem2/physics.html", {"info": data})


def manufPage(request):
    data = get_course_info("Manufacturing")
    return render(request, "sem2/manuf.html", {"info": data})


def mechaPage(request):
    data = get_course_info("Mechatronics")
    return render(request, "sem2/mecha.html", {"info": data})


def englishPage(request):
    data = get_course_info("Communication")
    return render(request, "sem2/english.html", {"info": data})


# Sem 3
def sem3Page(request):
    return render(request, "sem3.html")


def aimlPage(request):
    data = get_course_info("Artificial Intelligence")
    return render(request, "sem3/aiml.html", {"info": data})


def dsaPage(request):
    data = get_course_info("Data Structures")
    return render(request, "sem3/dsa.html", {"info": data})


def dscsPage(request):
    data = get_course_info("Discrete Structures")
    return render(request, "sem3/dscs.html", {"info": data})


def otPage(request):
    data = get_course_info("Optimization Techniques")
    return render(request, "sem3/ot.html", {"info": data})


def caoPage(request):
    data = get_course_info("Computer Architecture")
    return render(request, "sem3/cao.html", {"info": data})


# Sem 4
def sem4Page(request):
    return render(request, "sem4.html")


def cnPage(request):
    data = get_course_info("Computer Networks")
    return render(request, "sem4/cn.html", {"info": data})


def osPage(request):
    data = get_course_info("Operating Systems")
    return render(request, "sem4/os.html", {"info": data})


def adaPage(request):
    data = get_course_info("Analysis and Design of A")
    return render(request, "sem4/ada.html", {"info": data})


def psychoPage(request):
    data = get_course_info("Psychology")
    return render(request, "sem4/psycho.html", {"info": data})


def finPage(request):
    data = get_course_info("Finance")
    return render(request, "sem4/fin.html", {"info": data})


# Sem 5
def sem5Page(request):
    return render(request, "sem5.html")


def sePage(request):
    data = get_course_info("Software Engineering")
    return render(request, "sem5/se.html", {"info": data})


def scPage(request):
    data = get_course_info("Soft Computing")
    return render(request, "sem5/sc.html", {"info": data})


def tocPage(request):
    data = get_course_info("Theory of Computation")
    return render(request, "sem5/toc.html", {"info": data})


def mlPage(request):
    data = get_course_info("Machine Learning")
    return render(request, "sem5/ml.html", {"info": data})


def wircPage(request):
    data = get_course_info("Web IR Crawling")
    return render(request, "sem5/wirc.html", {"info": data})


# Sem 6
def sem6Page(request):
    return render(request, "sem6.html")


# Sem 7
def sem7Page(request):
    return render(request, "sem7.html")


# Sem 8
def sem8Page(request):
    return render(request, "sem8.html")


def get_course_info(course_name):
    try:
        course = Course.objects.get(course_name=course_name)

        return course
    except Course.DoesNotExist:
        return JsonResponse({"message": "Course not found"}, status=404)
    except Exception as e:
        return JsonResponse({"message": "Internal server error"}, status=500)


def crawlerPage(request):
    keyword = ""
    if request.method == "POST":
        keyword = request.POST.get("keyword", "")
    content_paragraph = ""

    def google_search(keyword, num_results=5, preferred_websites=None):
        base_url = "https://www.google.com/search"
        params = {"q": keyword}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error accessing Google search: {e}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        search_results = []

        for i, result in enumerate(soup.find_all("a", href=True), start=1):
            link = result["href"]
            if link.startswith("/url?"):
                # Extract the actual URL from the Google search result link
                actual_url = requests.utils.unquote(link.split("=")[1].split("&")[0])
                search_results.append(actual_url)
                if i == num_results:
                    break

        # Prioritize links from preferred websites
        if preferred_websites:
            for website in preferred_websites:
                for i, link in enumerate(search_results):
                    if website in link:
                        # Move the link to the top of the list
                        search_results.insert(0, search_results.pop(i))
                        break

        return search_results

    def crawl_website(url, keyword):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract a paragraph related to the keyword
        paragraphs = soup.find_all("p")
        relevant_paragraph = None

        for paragraph in paragraphs:
            if keyword.lower() in paragraph.get_text().lower():
                relevant_paragraph = paragraph.get_text()
                break

        return relevant_paragraph

    # Example usage
    keyword_to_search = keyword
    preferred_websites = [
        "https://www.geeksforgeeks.org/",
        "https://www.w3schools.com/",
        "https://stackoverflow.com/",
        "https://www.wikipedia.org",
        "https://www.youtube.com",
    ]
    top_links = google_search(
        keyword_to_search, num_results=5, preferred_websites=preferred_websites
    )

    print(f"Top {len(top_links)} links for '{keyword_to_search}':")
    for i, link in enumerate(top_links, start=1):
        print(f"{i}. {link}")

    # Example Wikipedia link (replace with the desired Wikipedia link)
    wikipedia_link = "https://en.wikipedia.org/"

    # Prioritize Wikipedia link and crawl to extract a paragraph related to the keyword
    if wikipedia_link in top_links:
        top_links.remove(wikipedia_link)  # Remove the Wikipedia link from the list
        top_links.insert(0, wikipedia_link)  # Insert it at the beginning

    # Flag to check if Wikipedia paragraph has been printed
    wikipedia_paragraph_printed = False

    for i, link in enumerate(top_links, start=1):
        # print(f"\nCrawling {link}:")

        # Check if the link is a Wikipedia link
        is_wikipedia_link = "wikipedia.org" in link

        # Crawl the website and extract a paragraph
        if is_wikipedia_link and not wikipedia_paragraph_printed:
            website_paragraph = crawl_website(link, keyword_to_search)
            if website_paragraph:
                print(f"   Wikipedia paragraph related to '{keyword_to_search}':")
                print(website_paragraph)
                content_paragraph = website_paragraph
                wikipedia_paragraph_printed = True  # Set the flag to True after printing the first Wikipedia paragraph
            else:
                print("   Unable to retrieve Wikipedia paragraph.")
        # elif not is_wikipedia_link:
        #     print(f"   Not a Wikipedia link.")

    return render(
        request,
        "crawler.html",
        {
            "content": content_paragraph,
            "links": top_links,
            "keyword": keyword_to_search,
        },
    )


@csrf_exempt
def update_material_status(request):
    if request.method == "POST":
        material = request.POST.get("material")
        status = request.POST.get("status")  # 'checked' or 'unchecked'
        course_id = request.POST.get("id")

        # Get the course instance, assuming you have a specific course identified
        # You may need to adjust this based on how you identify the course in your system

        course = Course.objects.get(pk=course_id)

        # Update the corresponding material field based on the status
        if material == "ppt":
            course.ppt_completed = status == "checked"
        elif material == "notes":
            course.notes_completed = status == "checked"
        elif material == "end_term":
            course.end_term_completed = status == "checked"
        elif material == "mid_term":
            course.mid_term_completed = status == "checked"
        elif material == "lab_files":
            course.lab_files_completed = status == "checked"

        # Save the changes to the database
        course.save()

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})
