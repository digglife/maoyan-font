import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='maoyan_font',
    version='2018.12',
    author='Zhu Sheng Li',
    author_email='digglife@gmail.com',
    description='将猫眼电影网页中票房、评分等数据的乱码转化成正常数字。',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/digglife/maoyan-font',
    packages=setuptools.find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=['requests', 'fonttools'],
)
