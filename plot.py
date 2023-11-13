import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data

####line chart: Belastung einr Partnerschaft mit Kind###
def plot_line_chart_emojis_words_partner_one_and_two(df):
    x = ['2017', '2018', '2019', '2020', '2021', '2022']

    df_janine = df[df['Name'] == "Janine"]
    df_stephie = df[df['Name'] == "Stephie"]

    y_3 = df_janine.groupby('Year').sum()['word_count']
    y_4 = df_stephie.groupby('Year').sum()['word_count']
    y_5 = df_janine.groupby('Year').sum()['EmojiCount']
    y_6 = df_stephie.groupby('Year').sum()['EmojiCount']

    bg_img_path = get_sample_data("images/background_image_whatsapp_black.png")
    bg_img = plt.imread(bg_img_path)

    fig1, ax1 = plt.subplots(figsize=(10, 6))

    # Plotting line charts
    ax1.plot(x, y_3, color="#009688", label='Wörter Janine', linestyle='solid', linewidth=2, alpha=1.0)
    ax1.plot(x, y_4, color="#06e744", label='Wörter Stephie', linestyle='solid', linewidth=2, alpha=1.0)
    ax1.plot(x, y_5, color="#009688", label='Emojis Janine', linestyle='dashed', linewidth=2, alpha=1.0)
    ax1.plot(x, y_6, color="#06e744", label='Emojis Stephie', linestyle='dashed', linewidth=2, alpha=1.0)

    # Setting labels and title
    plt.xlabel("Lebensmomente", fontsize=12)
    plt.ylabel("Anzahl", fontsize=12)
    plt.legend(fontsize=12)

    title_string = 'Belastung einer Partnerschaft mit Kind'
    subtitle_string = 'Die Daten wurden einem Whatsapp-Chat entnommen. Sie zeigen \neine emotionale Reduktion (Diversität der Emojis) und eine subjektiv verschieden \nempfundene Stressbelastung (Verminderung der Wortanzahl) bei einem Partner.'
    plt.title(subtitle_string, fontsize=12, x=0.5, y=1.0)
    plt.suptitle(title_string, fontsize=16, fontweight='bold', x=0.5, y=1.04)

    # Removing lines in the chart
    plt.gca().spines['top'].set_visible(False)

    # Adding a footnote
    footnote = "Quelle: Wiesemann, April 2023"
    ax1.text(x=0.75, y=0.00, s=footnote, fontsize=8, ha='left', transform=fig1.transFigure)

    # Changing the x-labels from numerical to categorical
    ax1.set_xticks(range(len(x)))
    ax1.set_xticklabels(('Beziehung', 'Umzug', 'Hochzeit', 'Geburt', '1.Lebensjahr', '2.Lebensjahr'))

    ax2 = ax1.twinx()

    # Creating bar chart for unique Emojis
    y_5_unique = [102, 130, 104, 53, 49, 74]
    ax2.bar(x, y_5_unique, color="#51585c", label='Unique Emojis', width=0.3, alpha=0.5)

    # Setting labels and title for bar plots
    ax2.set_ylabel("Diversität der Emojis", fontsize=12)

    # Adjusting the y-axis scale of ax2
    ax2.set_ylim(0, 500)

    # Removing lines in the chart
    plt.gca().spines['top'].set_visible(False)

    # Displaying the background image
    imagebox = OffsetImage(bg_img, zoom=1.25, resample=True, alpha=0.2)
    ab = AnnotationBbox(imagebox, (0.5, 0.5), frameon=False, pad=0.0, xycoords='axes fraction')
    ax1.add_artist(ab)

    # Adding arrow annotation
    arrow1_index = x.index('2020')
    arrow1_y = 3000
    arrow1_text = 'Sprachlosigkeit'

    ax1.annotate(arrow1_text,
                 xy=(arrow1_index, arrow1_y),
                 xytext=(arrow1_index - 0.1, arrow1_y + 3000),
                 arrowprops=dict(arrowstyle='->'),
                 fontsize=12)

    plt.show()

####line chart: Whatsapp-Kommunikation im Wandel######
def plot_line_chart_whatsapp(df):
    # Loading the separated datasets
    msg_stephie = df[df['Name'] == "Stephie"]
    msg_janine = df[df['Name'] == "Janine"]

    # Grouping the data by year and counting the number of occurrences
    stephie_counts = msg_stephie.groupby('Year').count()['Text']
    janine_counts = msg_janine.groupby('Year').count()['Text']

    bg_img_path = get_sample_data("images/background_image_whatsapp_black.png")
    bg_img = plt.imread(bg_img_path)

    # Creating a plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plotting the line chart
    plt.plot(stephie_counts.index, stephie_counts, color="#009688", label='Partner 1', linestyle='solid', linewidth=2)
    plt.plot(janine_counts.index, janine_counts, color="#06e744", label='Partner 2', linestyle='dashed', linewidth=2)

    # Adding labels
    plt.xlabel('Jahr', fontsize=12)
    plt.ylabel('Anzahl der Nachrichten', fontsize=12)

    # Adding title
    title_string = 'Whatsapp-Kommunikation im Wandel'
    subtitle_string = 'Die Daten wurden einem Whatsapp-Chats entnommen und ausgewertet.'
    plt.title(subtitle_string, fontsize=10)
    plt.suptitle(title_string, fontsize=14, fontweight='bold')

    # Adding a legend
    plt.legend()

    # Removing lines in the chart
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)

    # Adding a footnote
    footnote = "Quelle: Wiesemann, April 2023"
    ax.text(x=0.70, y=0.00, s=footnote, fontsize=9, ha='left', transform=fig.transFigure)

    # Adding arrow annotations
    def add_arrow_annotation(ax, x, y, text, xytext_x, xytext_y):
        ax.annotate(text,
                    xy=(x, y),
                    xytext=(xytext_x, xytext_y),
                    arrowprops=dict(arrowstyle='->'),
                    fontsize=12)

    add_arrow_annotation(ax, 2018, 5230, 'Umzug', 2017, 5280)
    add_arrow_annotation(ax, 2019, 4900, 'Hochzeit', 2019.2, 5200)
    add_arrow_annotation(ax, 2020, 990, 'Geburt', 2020.5, 1990)

    # Display the background image
    imagebox = OffsetImage(bg_img, zoom=1.2, resample=True, alpha=0.2)
    ab = AnnotationBbox(imagebox, (0.5, 0.5), frameon=False, pad=0.0, xycoords='axes fraction')
    ax.add_artist(ab)

    plt.show()

###radar chart: Tägliche Whatsapp-Kommunikation###
def radar_chart_pro_year():
    # Data
    categories = ['06:00', '05:00', '04:00', '03:00', '02:00', '01:00', '00:00', '23:00', '22:00', '21:00', '20:00', '19:00', '18:00', '17:00', '16:00', '15:00', '14:00', '13:00', '12:00', '11:00', '10:00', '09:00', '08:00', '07:00']
    values1 = [14, 0, 0, 0, 0, 0, 9, 55, 344, 309, 281, 333, 278, 335, 250, 343, 421, 326, 263, 268, 274, 242, 223, 260]
    values4 = [5, 0, 2, 0, 0, 0, 0, 17, 59, 85, 151, 122, 66, 143, 176, 156, 215, 325, 428, 325, 139, 155, 110, 65]

    num_categories = len(categories)

    # Find the index of '15:00' in the categories list
    start_index = categories.index('15:00')

    # Reorder the categories and values to start with '15:00'
    categories = categories[start_index:] + categories[:start_index]
    values1 = values1[start_index:] + values1[:start_index]
    values4 = values4[start_index:] + values4[:start_index]

    # Calculate angles for each category in a clockwise manner
    angles = np.linspace(0, 2*np.pi, num_categories, endpoint=False).tolist()
    angles += angles[:1]  # Close the loop

    # Append the first value to the end to close the shape
    values1 += values1[:1]
    values4 += values4[:1]

    bg_img_path = get_sample_data("images/background_image_whatsapp_black.png")
    bg_img = plt.imread(bg_img_path)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Plot the spider web lines with transparency
    ax.plot(angles, values1, linewidth=1, linestyle='solid', color='black', alpha=0.3)
    ax.plot(angles, values4, linewidth=1, linestyle='solid', color='black', alpha=0.3)

    # Plot the first dataset (2017)
    ax.plot(angles, values1, 'o-', linewidth=1.0, linestyle='solid', color='#06e744', label='Beziehungsstart', alpha=0.8)
    ax.fill(angles, values1, color='#06e744', alpha=0.4)

    # Plot the third dataset (2019)
    ax.plot(angles, values4, 'o-', linewidth=1.0, linestyle='solid', color='#009688', label='Geburt', alpha=0.8)
    ax.fill(angles, values4, color='#009688', alpha=0.4)

    # Set the category labels
    plt.xticks(angles[:-1], categories, color='black', size=12)

    # Set the y-axis ticks and labels
    max_value = max(max(values1), max(values4))
    plt.yticks(np.arange(0, max_value+500, 500), color='black', size=10, weight="bold")

    # Set the title and legend
    title_string = 'Tägliche Whatsapp-Kommunikation'
    subtitle_string = 'Nach der Geburt eines Kindes verengt sich \nder Kommunikationszeitraum auf den Mittagsschlaf des Kindes.'
    plt.title(subtitle_string, fontsize=12, x=0.5, y=1.1)
    plt.suptitle(title_string, fontsize=16, fontweight='bold', x=0.5, y=1.09)

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

    # Add a footnote
    footnote = 'Quelle: Wiesemann, Juni 2023'
    plt.annotate(footnote, xy=(0.5, -0.15), xycoords='axes fraction', ha='center', fontsize=8)

    # Display the background image
    imagebox = OffsetImage(bg_img, zoom=1.1, resample=True, alpha=0.2)
    ab = AnnotationBbox(imagebox, (0.5, 0.5), frameon=False, pad=0.0, xycoords='axes fraction')
    ax.add_artist(ab)

    # Display the plot
    plt.show()
