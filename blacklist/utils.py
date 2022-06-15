from blacklist.models import BlacklistedEmail, BlacklistedPhoneNumber, BlacklistedPassword

def banned_passwords():
    """
    Return a list of banned passwords.
    """
    banned_passwords = BlacklistedPassword.objects.all().values_list('plaintext_password', flat=True)
    return list(set(banned_passwords))

def banned_emails():
    """
    Return a list of banned emails.
    """
    banned_emails = BlacklistedEmail.objects.all().values_list('email', flat=True)
    return list(set(banned_emails))

def banned_phone_numbers():
    """
    Return a list of banned phone numbers.
    """
    banned_phone_numbers = BlacklistedPhoneNumber.objects.all().values_list('phone_number', flat=True)
    return list(set(banned_phone_numbers))