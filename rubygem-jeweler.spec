#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-jeweler
Version  : 2.0.1
Release  : 5
URL      : https://rubygems.org/downloads/jeweler-2.0.1.gem
Source0  : https://rubygems.org/downloads/jeweler-2.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-jeweler-bin
BuildRequires : ruby
BuildRequires : rubygem-bluecloth
BuildRequires : rubygem-builder
BuildRequires : rubygem-git
BuildRequires : rubygem-github_api
BuildRequires : rubygem-highline
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-yard

%description
# Jeweler: Craft the perfect RubyGem
Jeweler provides the noble ruby developer with two primary features:

%package bin
Summary: bin components for the rubygem-jeweler package.
Group: Binaries

%description bin
bin components for the rubygem-jeweler package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n jeweler-2.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-jeweler.gemspec

%build
gem build rubygem-jeweler.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
jeweler-2.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/jeweler-2.0.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/.coveralls.yml
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/.document
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/ChangeLog.markdown
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/README.markdown
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/bin/jeweler
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/cucumber.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/directory_layout.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/dotdocument.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/env_options.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/gemfile.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/git.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/license.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/rakefile.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/readme.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/test.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/generator/test_helper.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/placeholder.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/step_definitions/debug_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/step_definitions/filesystem_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/step_definitions/generator_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/step_definitions/task_steps.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/support/env.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/tasks/build_gem.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/tasks/version.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/features/tasks/version_bumping.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/jeweler.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/build_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/check_dependencies.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/install_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/release_gemspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/release_to_git.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/release_to_rubygems.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/validate_gemspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/version/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/version/bump_major.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/version/bump_minor.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/version/bump_patch.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/version/write.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/commands/write_gemspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/gemcutter_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/gemspec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/application.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/bacon_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/github_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/micronaut_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/minitest_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/rdoc_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/riot_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/rspec_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/shindo_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/shoulda_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/testspec_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/testunit_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/generator/yard_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/rubyforge_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/rubygems_dot_org_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/rubygems_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/specification.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/.document
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/bacon/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/bacon/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/bundler_setup.erb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/features/default.feature
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/features/support/env.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/jeweler_tasks.erb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/micronaut/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/micronaut/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/minitest/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/minitest/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/other_tasks.erb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/riot/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/riot/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/rspec/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/rspec/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/rspec/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/shindo/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/shindo/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/shoulda/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/shoulda/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/simplecov.erb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/testspec/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/testspec/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/testunit/flunking.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/templates/testunit/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/lib/jeweler/version_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/bar/VERSION.yml
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/bar/bin/foo_the_ultimate_bin
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/bar/hey_include_me_in_gemspec
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/bar/lib/foo_the_ultimate_lib.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/.document
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/existing-project-with-version.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/lib/existing_project_with_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/test/existing_project_with_version_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-constant/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/.document
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/existing-project-with-version.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/lib/existing_project_with_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/test/existing_project_with_version_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-plaintext/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/.document
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/VERSION.yml
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/bin/foo_the_ultimate_bin
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/existing-project-with-version.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/lib/existing_project_with_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/test/existing_project_with_version_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/fixtures/existing-project-with-version-yaml/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/geminstaller.yml
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/test_build_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/test_install_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/test_release_to_gemcutter.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/test_release_to_git.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/test_release_to_github.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/test_validate_gemspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/test_write_gemspec.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/version/test_base.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/version/test_bump_major.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/version/test_bump_minor.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/version/test_bump_patch.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/commands/version/test_write.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/generator/test_application.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/generator/test_options.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/test_gemspec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/test_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/test_generator_initialization.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/test_generator_mixins.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/test_specification.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/test_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/jeweler/test_version_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/shoulda_macros/jeweler_macros.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/jeweler-2.0.1/test/test_jeweler.rb
/usr/lib64/ruby/gems/2.3.0/specifications/jeweler-2.0.1.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/jeweler
