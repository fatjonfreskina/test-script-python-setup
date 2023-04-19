from distutils.core import setup

setup(name='test-script',
      version='1.0',
      description='Just print hello world',
      license='UNIPD',
      author='Fatjon Freskina',
      author_email='fatjonfreskina@gmail.com',
      install_requires=[
        'pandas', 'numpy'],
      py_modules=["test"],
      entry_points={"console_scripts": ["test=test:main"]},
)
