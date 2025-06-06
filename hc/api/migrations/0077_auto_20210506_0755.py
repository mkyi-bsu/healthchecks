# Generated by Django 3.2.1 on 2021-05-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0076_auto_20201128_0951"),
    ]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="kind",
            field=models.CharField(
                choices=[
                    ("email", "Email"),
                    ("webhook", "Webhook"),
                    ("hipchat", "HipChat"),
                    ("slack", "Slack"),
                    ("pd", "PagerDuty"),
                    ("pagertree", "PagerTree"),
                    ("pagerteam", "Pager Team"),
                    ("po", "Pushover"),
                    ("pushbullet", "Pushbullet"),
                    ("opsgenie", "Opsgenie"),
                    ("victorops", "Splunk On-Call"),
                    ("discord", "Discord"),
                    ("telegram", "Telegram"),
                    ("sms", "SMS"),
                    ("zendesk", "Zendesk"),
                    ("trello", "Trello"),
                    ("matrix", "Matrix"),
                    ("whatsapp", "WhatsApp"),
                    ("apprise", "Apprise"),
                    ("mattermost", "Mattermost"),
                    ("msteams", "Microsoft Teams"),
                    ("shell", "Shell Command"),
                    ("zulip", "Zulip"),
                    ("spike", "Spike"),
                    ("call", "Phone Call"),
                    ("linenotify", "LINE Notify"),
                    ("signal", "Signal"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="check",
            name="subject",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="check",
            name="subject_fail",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
