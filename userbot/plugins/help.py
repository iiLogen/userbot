from userbot import UserBot, CMD_HELP
from pyrogram import Filters, Message


@UserBot.on_message(Filters.command("help", ".") & Filters.me)
async def module_help(bot: UserBot, message: Message):
    cmd = message.command

    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) is 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) is 1:
        await message.edit("Please specify which module you want help for!! \nUsage: .help <module_name>", parse_mode=None)

        all_commands = ""
        for x in CMD_HELP:
            all_commands += f"`{str(x)}`\n"

        await message.reply(all_commands)
        return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = ""
            this_command += f"--**Help for {str(help_arg)} module**--\n".upper()

            for x in commands:
                this_command += f"**{str(commands[x]['command'])}**: ```{str(commands[x]['description'])}```\n\n"

            await message.edit(this_command, parse_mode='markdown')
        else:
            await message.edit('`Please specify a valid module name.`', parse_mode='markdown')


def add_command_help(module_name, commands):
    """
    Adds a modules help information.
    :param module_name: name of the module
    :param commands: list of lists, with command and description each.
    """
    temp_dict = {}
    count = 1
    for x in commands:
        another_dict = {'command': x[0], 'description': x[1]}
        temp_dict[count] = another_dict
        count += 1

    CMD_HELP[module_name] = temp_dict
