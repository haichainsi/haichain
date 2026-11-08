for path in ['dashboard.html', 'app/dashboard.html', 'index.html', 'app/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('pdf-modal.js?v=v65_institutional_tables_math_fixed_20261103', 'pdf-modal.js?v=v66_dual_resend_email_backend_20261103')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Bumped cache in", path)
